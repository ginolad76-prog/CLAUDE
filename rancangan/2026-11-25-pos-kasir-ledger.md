# SDD ledger — plan: /home/user/CLAUDE/rancangan/2026-11-25-pos-kasir-plan.md
Spec: /home/user/CLAUDE/rancangan/2026-11-25-pos-kasir-design.md
Repo kerja: /home/user/tokotehtjapduakoi.github.io, branch claude/pos-toko-teh-tjap-dua-koi-1mze9t, start 11f7ea6

## Pre-flight scan
| Tasks | Shared | Finding |
|---|---|---|
| T1 self | db.py/conftest | ok; test_klaim_nota_lama uses pemilik+aal2 so survives T2 |
| T1–T2 | kolam/setup.sql via Db.baru | ok |
| T1–T7 | storage.objects tiruan | T7 storage_mb needs size; tiruan lacks metadata → Ruling A |
| T1–T8 | db.py CLI `--buat` | T1 doesn't specify CLI → Ruling B |
| T2 self | kk_claim_code status list vs tests | ok |
| T2–T4 | kk_receipts code cols, created_by | ok |
| T2–T13 | kk_set_staff phone, kk_settings | ok (default arg keeps admin.js working until T13) |
| T3 self | pos_me shift null until T5 | ok |
| T3–T4 | pos_device_ok, price_history | ok |
| T4 self | rule 10 total=0 creates kk_receipts, but kk_receipts.total check(total>0) | conflict → Ruling C |
| T4–T5 | T4 tests need open shift; pos_shifts defined in T5 | conflict → Ruling D |
| T4–T6 | pos_notas status/voided_at; trigger allows those cols | ok |
| T4–T7 | pos_notas fields used by report | ok |
| T5 self | ok |
| T6 self | ok |
| T8 self | server tiruan aal2 by email prefix | ok |
| T8–T9..T13 | bantu.mjs seed, KASIR_CONFIG route | ok |
| T9–T10 | Lunas flow: T9 calls checkout direct, T10 routes through Antrean | ok (T10 modifies) |
| T9 self | WA text "berlaku 7 hari" only valid when phone bound — WA only shown when phone given | ok |
| T10 self | sw caching ../kolam/vendor from kasir scope | ok (controlled client fetches intercepted) |
| T11–T5 | shift fns | ok |
| T12 self | MFA enroll not e2e-testable on tiruan | accepted; manual check in T14 |
| T13–T2 | kk_claim_code statuses | ok |
| T14 | live smoke needs owner action + credential | stop point (security-sensitive: credential) |

Ruling A: tiruan storage.objects gets `metadata jsonb` (Supabase has it, size in metadata->>'size'); pos_report sums it — matches real Supabase — cost if wrong: storage_mb null.
Ruling B: Task 8 adds `python3 _uji/db.py --buat` CLI (prints conninfo, seeds sample data) — T8 owns its consumer — low cost.
Ruling C: total=0 (all free via voucher) → no kk_receipts row, no code; output code_status 'tidak_ada', expires_at null; UI hides QR — spec: pulls only from total, check constraint forbids 0 — cost: none.
Ruling D: pos_shifts table created in Task 4 (table + RLS only; shift_id FK); Task 5 adds functions/rules. T4 tests insert an open shift as superuser. — cost: none.

Task 1: implemented 12066cd (implementer a761522e79f125ac7)
Task 1: minor (deferred): conftest dir leak if initdb fails before try; fixed port 54329
Task 1: minor (deferred): storage.buckets/objects lack some real columns (file_size_limit, owner_id...)
Task 1: minor (deferred): test_rls_berlaku_dan_foldername bundles two checks + unused db.user
Task 1: minor (deferred): sql() runs as postgres session so tests can `reset role` (README note)
Task 1: fix round 1 dispatched (Important: default grants worst-case; NULL/multiline in sql())
Task 1: fix round 1/5 (2 addressed, 0 open; commits 12066cd..d4081a9)
Task 1: minor (deferred): db.sql trailing-RS strip can drop a last empty-string row; multi-statement q concatenates
Task 1: complete (commits 11f7ea6..d4081a9, review clean)
Harness notes for later tasks: db.sql returns tuples of str|None; single-row single-empty-string reads as []; worst-case default grants (anon/authenticated ALL on public tables) — security tests must rely on revoke/RLS.
Task 2: dispatched implementer ace6ead957149d4c4, BASE d4081a9
Task 2: implemented 5e4e792 (DONE_WITH_CONCERNS)
Ruling E: admin.js owner functions need aal2 after Task 2 → Task 13 must add a 2-step (TOTP) verify step to Admin Kolam Koi (same pattern as Task 12) and staff phone field; live SQL deploy only happens in Task 14 after UI ready — cost if wrong: owner locked out of admin until T13.
Task 2: complete (commits d4081a9..5e4e792, review clean)
Task 2: minor (deferred→carried to Task 4): staff can SELECT kk_receipts.code_hash → column-level grant excluding code_hash
Task 2: minor (deferred→carried to Task 4): legacy toggle fails open on missing row → coalesce(...,false)
Task 2: minor (deferred): legacy path leaks existence of coded notas without counting fails
Task 2: minor (deferred): staff_own only checks creator phone
Task 2: minor (deferred): no concurrency test for double claim
Task 2: minor (deferred): explicit revoke right after kk__draw creation
Task 3: dispatched, BASE 5e4e792
Task 3: implemented 9c4c70f (af71e325122263b4a)
Task 3: complete (commits 5e4e792..9c4c70f, review clean)
Task 3: minors carried to Task 4 part A (hardening): grant/sequence privilege tests; bucket do update set public=false; seed pay methods only when table empty; persen <=100 check; device id/label length cap + on conflict; kolam bulk revoke scoped to kk_% so rerun of kolam doesn't strip pos grants
Task 3: minor (deferred): audit old/new tested only for price; weak asserts test_pos_dasar:61,117; pos_me keys unasserted; search_path pg_temp; unvalidated save inputs/raw errors; no row lock in saves
Ruling F: carry the listed security-relevant minors from Tasks 2–3 into Task 4 as part A — owner priority is security; cheap; cost: slightly larger Task 4.
Task 4: dispatched, BASE 9c4c70f
Task 4: implemented 36a8b94 (a31f4111674a1f2eb, DONE_WITH_CONCERNS)
Task 14 check: confirm on real Supabase that definer functions (owner postgres) can read storage.objects (bypassrls) — pos_checkout depends on it
Task 4: review needs fixes (Important: offline inflated total→pulls; kk_delete_receipt on POS receipts; K-format legacy nota blocks checkout); fix round 1 dispatched to a31f4111674a1f2eb
Ruling G: offline mismatch → pos_notas.total = client total, kk_receipts.total = least(client, server) (spec 6.6 says code not held) — cost: customer may get fewer pulls than paid if server prices were wrong
Task 4: minor (deferred): voucher frees first line regardless of variant (plan-mandated); pulls recomputed on replay; raw cast errors; concurrent same-id/voucher untested; device id bearer string; checkout doesn't compare device to shift device (Task 5 decide)
Task 4: fix round 1/5 (3 addressed + minors, 0 open; commits 36a8b94..6a9750a)
Task 4: complete (commits 9c4c70f..6a9750a, review clean)
Ruling H: shift not bound to device (kasir may switch phones mid-shift, device approval still required per checkout) — spec allows moving phones — cost: none significant
Task 5: dispatched, BASE 6a9750a
Task 5: implemented 1e200c5 (a50a4b474649da886)
Task 5: review needs fixes (Important: photo reuse one-directional; receiver sees closer's count — plan-mandated); fix round 1 dispatched
Ruling I: handover_waiting.cash_counted visible to owner only (blind count per spec 6.9) — overrides plan interface — cost: none
Ruling J: offline nota attaches to the cashier's shift covering client_at (even if closed); lock shift row for key share — avoids stuck queue, makes shortfall visible — cost: closed shift expected changes after close (shown in report)
Carry to Task 7: flag when a new shift's cash_start differs from previous store-close cash_counted
Task 5: minor (deferred): pos_shift_expected NULL for unknown id; pos_me limit 1 without order by
Task 5: fix round 1/5 (3 addressed, 0 open; commits 1e200c5..aac68fa)
Task 5: complete (commits 6a9750a..aac68fa, review clean)
Carry to Task 6: pos_shift_close should take FOR UPDATE on the shift row (conflicts with checkout's FOR KEY SHARE) so close/checkout serialize
Task 6: dispatched, BASE aac68fa
Task 6: implemented 3b04cd7 (a9392ae83f0b74908, DONE_WITH_CONCERNS: no RED run; secret cards not reversed)
Task 6: complete (commits aac68fa..3b04cd7, review clean; RED run skipped — reviewer judged tests valid)
Task 6: minor (deferred): collection/secret bonus not reversed on void; no concurrency test; loose asserts test_pos_void:94,138
Carry to Task 7 part A: void decrements kk_members.trx by 1 and spent by receipt total (floor 0) when claimed; test pos_shift_expected drops after cash void
Task 7: dispatched, BASE 3b04cd7
Task 7: implemented 9d37a87 (a5cb24d14f3c83e00)
Task 7: review needs fixes (Important: WITA boundary test not discriminating); fix round 1 dispatched incl. rulings
Ruling K: pending_voids counts all open requests (any day); sargable day filter + client_at index — owner must not miss pending voids — cost: none
Task 7: minor (deferred): suspicious counts only 3rd+ claim; start_mismatch picks by max(id); kk_pulls proxy breaks if a tier had pulls=0
Task 7: fix round 1/5 (4 addressed, 0 open; commits 9d37a87..55a61a5)
Task 7: complete (commits 3b04cd7..55a61a5, review clean)
Task 7: minor (deferred): 00:30 WITA test early-returns ~2% of runs; stray `), )` test_pos_laporan.py:53
Ruling L: e2e tests use node:test + require('playwright') (preinstalled; do not install @playwright/test or browsers) run with `node --test e2e/`, replacing `npx playwright test` in plan — env constraint — cost: none
Task 8: dispatched, BASE 55a61a5
Task 8: implemented ee1d15c (a9fb60c5a76f09390); e2e cmd: cd _uji && node --test 'e2e/*.spec.mjs'
Task 8: complete (commits 55a61a5..ee1d15c, review clean)
Carry to Task 9: server_tiruan storage must parse multipart/FormData bodies (store real bytes; size test ≤40KB); esc(i.id) kasir.js:940; test that pointerdown resets idle timer
Task 8: minor (deferred): keluar(true) after failed device request with queue>0; no re-entrancy guard in idle check; CSP lacks base-uri/form-action (constraint-mandated string); _uji published on Pages (test-only secrets)
Task 9: dispatched, BASE ee1d15c
Task 9: implemented 9d04e3a (a3f52103fb05adf61; no RED run; discount/voucher e2e missing)
Task 9: review needs fixes (Important: code regenerated on same-id retry; photo 409 swallow keeps stale photo; no discount/voucher e2e); fix round 1 dispatched
Task 9: minor (deferred): rp exported via KasirKode; teksWa uses phone clock; foto.js cancel-event leak; duplicate css rule
Task 9: fix round 1/5 (3 addressed + extras, 0 open; commits 9d04e3a..68e2db5)
Task 9: complete (commits ee1d15c..68e2db5, review clean)
Task 9: minor (deferred): jual.spec shared DB state without cleanup; putus-setelah-rpc stays armed
Carry to Task 10: lock photo as soon as Lunas is pressed (nota enters queue), closing the residual upload-response-lost case
Task 10: dispatched, BASE 68e2db5
Task 10: implemented 61d4896 (ac8682910564fd851, DONE_WITH_CONCERNS)
Task 10: review needs fixes (Important: stuck item stops queue; queue not tagged per uid; error items block logout forever [plan-mandated]; Lunas waits on backlog w/o timeout); fix round 1 dispatched
Ruling M: Antrean.jumlah() for logout counts only non-error items; error items persist for Task 11 to show/resolve — security idle-logout wins — cost: error items need Task 11 UI
Ruling N: voucher notas resent with offline=false approved (vouchers only when online; idempotent) — cost: may become error item if shift closed
Task 10: minor (deferred): opaque font cache quota; no Promise.all trigger test; 30s interval only covered indirectly
Carry to Task 11: Nota tab shows error items (message) with "Laporkan ke pemilik" and a two-tap "Hapus dari HP" after reporting
Task 10: fix round 1/5 (4 addressed + extras, 0 open; commits 61d4896..6325b0a)
Task 10: complete (commits 68e2db5..6325b0a, review clean)
Task 10: minor (deferred): jwt-refresh path untested; no backlog+slow combined test; jalankan without uid sends all; uncleared 8s timer; rejected-after-timeout becomes error item
Task 11: dispatched, BASE 6325b0a
Task 11: implemented b8d277d (adf7faf6affc7b2a6; no RED; handover_waiting lacks cashier id)
Task 11: review needs fixes (Important: handover_waiting lacks is_mine → closer stuck after reload); fix round 1 dispatched
Task 11: minor (deferred): Antrean.hapus doesn't self-check error/ownership; sudahLapor honor-system; owner WA number public in config (owner's choice); kasir.js ~480 lines
Task 11: fix round 1/5 (1 addressed + extras, 0 open; commits b8d277d..c4b3c50)
Task 11: complete (commits 6325b0a..c4b3c50, review clean). Server-side self-receive rejection already tested in Task 5 test_serah_terima.
Task 12: dispatched, BASE c4b3c50
Task 12: implemented ac14575 (a8fd41585e275c6a9; MFA real enroll untested → Task 14)
Task 12: review needs fixes (Important: pos_report aal1 only); fix round 1 dispatched
Ruling O: pos_report requires kk_owner_mfa() (global constraint beats plan's "aal1 cukup") — cost: Dompet sync (later plan) must read via service key, not owner session
Task 12: minor (deferred): segarBadge swallows errors; simpan shows muatMe error after successful save; no positive cards_missing UI test
Task 12: fix round 1/5 (1 addressed + extras, 0 open; commits ac14575..d441b0e)
Task 12: complete (commits c4b3c50..d441b0e, review clean)
Task 12: minor (deferred): Setujui photo refetch only on tab enter/muat
Task 13: dispatched, BASE d441b0e (includes Ruling E: admin MFA step + staff phone)
Task 13: implemented 382eadf (ad3d594ffea78e75a; no RED; added GET /rest/v1/<table> to mock; legacy toggle read via sb.from fails open in UI)
Found: test_laporan_offline_selisih_tahan_dan_diskon flaky between 00:00–00:30 WITA (now-30min falls on previous WITA day) — test bug from Task 7, not code; fix: report day = WITA date of ts. Carry into Task 13 fix round.
Task 13: review needs fixes (Important: admin MFA retry loop; legacy UI fails open; lost code on transient failure) + flaky laporan test; fix round 1 dispatched
Task 13: minor (deferred): wrong_phone/staff_own only as toast; claim() label not restored
Task 13: fix round 1/5 (4 addressed + extras, 0 open; commits 382eadf..de53d2e)
Task 13: complete (commits d441b0e..de53d2e, review clean)
Task 14: dispatched (part 1: docs + full test + secret scan + write asap_asli.py, NOT run against live), BASE de53d2e. Live steps = stop point (owner runs SQL; credential).
Task 14 part1: implemented f8ad4cc (pytest 119, e2e 53). asap_asli leaves nota/lines/shift (lock triggers) → prints cleanup SQL for owner
Ruling P: Task 14 part 1 (docs + smoke script) reviewed inside the final whole-branch review instead of a separate task review — saves a seat; final reviewer told to cover it — cost: low
Final review: With fixes — 8 Important (deploy-order docs; phone guide; asap cleanup pollutes live; asap live grant checks; early revoke kk__draw; suspicious AND→OR; held release missing; service_role grants) + selected minors. One fix wave dispatched (list in final-findings.md).
Ruling Q: fix all 8 Important + 4 cheap minors in one wave; defer member-name lookup at checkout, owner two-phone login, proxy-behaviour confirm (done live) — cost: spec 6.4 member name not shown yet
Live check 26 Nov: proxy-injected secret works (role service_role) but live grants missing → 42501 on kk_cards; confirms final finding 8
Ruling R: suspicious = ≥3 claims of same creator's notas in 7 days (regardless of speed); <60s alone NOT flagged — normal QR scans at counter would flood warnings — cost: a single fast harvest not flagged unless repeated
Final fix wave re-review: all findings ADDRESSED; new Important in fix diff: asap_asli UJI-{rand} case mismatch leaves claimable live receipt
Ruling S: targeted one-off fix of asap_asli (uppercase RAND, verify deletion, cleanup SQL) before any live run — load-bearing for live safety — cost: none; verified by me via code read before running
Parked (owner-accepted risk, ruling a): kk_claim legacy path lacks staff_own; manual notas not in suspicious report — cost: kasir could self-claim manual ESB notas during transition
Final: minor (deferred): kk_set_* toggles toast success when settings row missing
Final fix: 4479d9e asap uppercase fix (verified by controller grep). main moved to 2bdc44e (Teman Tarik referral, new Kolam UI from another session) → merge dispatched (a0a18fa29151cfdb4)
Merge: 2b4169f..a861068 (pytest 157, e2e 55)
Merge2: bc559d6..80192c7 (pytest 161, e2e 55)
