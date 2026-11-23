-- Dompet Koi: database keuangan keluarga + Toko Teh
-- Jalankan sekali di Supabase: SQL Editor > New query > tempel semua > Run.

create extension if not exists pgcrypto;

create table if not exists public.households (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  invite_code text unique not null default upper(substr(md5(random()::text), 1, 6)),
  family_target bigint not null default 9000000,     -- batas pengeluaran keluarga per bulan
  shop_daily_target bigint not null default 1000000, -- target omzet toko per hari
  loan_total bigint not null default 100000000,      -- pinjaman mama
  created_at timestamptz not null default now()
);

create table if not exists public.members (
  household_id uuid not null references public.households on delete cascade,
  user_id uuid not null references auth.users on delete cascade,
  display_name text not null default 'Anggota',
  joined_at timestamptz not null default now(),
  primary key (household_id, user_id)
);

create table if not exists public.transactions (
  id uuid primary key default gen_random_uuid(),
  household_id uuid not null references public.households on delete cascade,
  book text not null check (book in ('keluarga', 'toko')),
  kind text not null check (kind in ('keluar', 'masuk')),
  amount bigint not null check (amount > 0),
  category text not null,
  note text,
  tx_date date not null default current_date,
  created_by uuid not null default auth.uid() references auth.users,
  created_at timestamptz not null default now()
);
create index if not exists transactions_household_date on public.transactions (household_id, tx_date);

create table if not exists public.budgets (
  household_id uuid not null references public.households on delete cascade,
  category text not null,
  amount bigint not null default 0 check (amount >= 0),
  primary key (household_id, category)
);

-- Apakah user yang login anggota rumah tangga ini?
create or replace function public.is_member(h uuid) returns boolean
language sql security definer stable set search_path = public as $$
  select exists (select 1 from members where household_id = h and user_id = auth.uid());
$$;

alter table public.households enable row level security;
alter table public.members enable row level security;
alter table public.transactions enable row level security;
alter table public.budgets enable row level security;

drop policy if exists hh_read on public.households;
drop policy if exists hh_update on public.households;
create policy hh_read on public.households for select using (public.is_member(id));
create policy hh_update on public.households for update using (public.is_member(id)) with check (public.is_member(id));

drop policy if exists mem_read on public.members;
drop policy if exists mem_update_self on public.members;
create policy mem_read on public.members for select using (public.is_member(household_id));
create policy mem_update_self on public.members for update using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists tx_all on public.transactions;
create policy tx_all on public.transactions for all
  using (public.is_member(household_id)) with check (public.is_member(household_id));

drop policy if exists bud_all on public.budgets;
create policy bud_all on public.budgets for all
  using (public.is_member(household_id)) with check (public.is_member(household_id));

-- Buat rumah tangga baru, pembuatnya otomatis jadi anggota.
create or replace function public.create_household(p_name text, p_display text) returns uuid
language plpgsql security definer set search_path = public as $$
declare h uuid;
begin
  if auth.uid() is null then raise exception 'Belum login'; end if;
  insert into households (name) values (coalesce(nullif(trim(p_name), ''), 'Keluarga')) returning id into h;
  insert into members (household_id, user_id, display_name) values (h, auth.uid(), coalesce(nullif(trim(p_display), ''), 'Anggota'));
  insert into budgets (household_id, category, amount) values
    (h, 'Cicilan mama', 1400000),
    (h, 'Langganan (Claude dll)', 500000);
  return h;
end $$;

-- Gabung pakai kode undangan 6 huruf.
create or replace function public.join_household(p_code text, p_display text) returns uuid
language plpgsql security definer set search_path = public as $$
declare h uuid;
begin
  if auth.uid() is null then raise exception 'Belum login'; end if;
  select id into h from households where invite_code = upper(trim(p_code));
  if h is null then raise exception 'Kode undangan tidak ditemukan'; end if;
  insert into members (household_id, user_id, display_name)
    values (h, auth.uid(), coalesce(nullif(trim(p_display), ''), 'Anggota'))
    on conflict (household_id, user_id) do nothing;
  return h;
end $$;

revoke all on function public.create_household(text, text) from public, anon;
revoke all on function public.join_household(text, text) from public, anon;
grant execute on function public.create_household(text, text) to authenticated;
grant execute on function public.join_household(text, text) to authenticated;
grant execute on function public.is_member(uuid) to authenticated;

-- Supaya HP satu langsung melihat catatan dari HP lain.
do $$ begin
  alter publication supabase_realtime add table public.transactions;
exception when duplicate_object then null; end $$;
do $$ begin
  alter publication supabase_realtime add table public.budgets;
exception when duplicate_object then null; end $$;
