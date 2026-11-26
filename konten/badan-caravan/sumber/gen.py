import re,sys
G='#0E4D32';GD='#0A3A26';M='#7A1F2B';Au='#C9A24B';K='#F6EFDF';R='#B3261E'
logo=open('logo.svg').read()
logo=re.sub(r'<\?xml.*?\?>|<!--.*?-->','',logo,flags=re.S).strip()
logo=logo.replace('<svg ','<svg id="lg" ',1)
def L(x,y,d):  # place logo
    l=re.sub(r'width="3200" height="3200"',f'x="{x}" y="{y}" width="{d}" height="{d}"',logo,count=1)
    c=(x+d/2,y+d/2); r=d/2
    halo=f'<circle cx="{c[0]}" cy="{c[1]}" r="{r*1.06}" fill="{K}"/><circle cx="{c[0]}" cy="{c[1]}" r="{r*1.025}" fill="{G}" stroke="{Au}" stroke-width="{d*.008}"/>'
    return halo+l.replace('id="lg" ','',1)
MASKOT='''<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<g fill="%(K)s" stroke="%(K)s" stroke-width="26">
<circle cx="240" cy="82" r="32"/><circle cx="240" cy="200" r="74"/>
<path d="M162 268 Q160 262 172 262 L308 262 Q320 262 320 274 L346 538 Q348 556 330 556 L150 556 Q132 556 134 538 Z"/></g>
<circle cx="240" cy="82" r="30" fill="%(K)s" stroke="%(G)s" stroke-width="9"/>
<path d="M272 96 Q292 72 322 88 Q300 112 272 96 Z" fill="%(M)s"/>
<path d="M162 270 L318 270 L342 540 L138 540 Z" fill="%(K)s" stroke="%(G)s" stroke-width="9"/>
<circle cx="240" cy="200" r="70" fill="%(K)s" stroke="%(G)s" stroke-width="9"/>
<path d="M176 168 Q240 120 304 168" stroke="%(G)s" stroke-width="7"/>
<path d="M208 214 Q218 202 228 214 M252 214 Q262 202 272 214" stroke="%(G)s" stroke-width="7"/>
<path d="M216 234 Q240 254 264 234" stroke="%(G)s" stroke-width="7"/>
<circle cx="196" cy="230" r="11" fill="#EBA594"/><circle cx="284" cy="230" r="11" fill="#EBA594"/>
<path d="M176 292 Q240 330 304 292" stroke="%(M)s" stroke-width="9"/>
<path d="M262 322 L248 368" stroke="%(M)s" stroke-width="8"/>
<path d="M190 350 L222 424 M290 350 L258 424" stroke="%(G)s" stroke-width="26"/>
<path d="M190 350 L222 424 M290 350 L258 424" stroke="%(K)s" stroke-width="12"/>
<path d="M214 378 L266 378 L260 458 L220 458 Z" fill="#B9824F" stroke="%(G)s" stroke-width="8"/>
<rect x="206" y="366" width="68" height="14" rx="3" fill="%(K)s" stroke="%(G)s" stroke-width="8"/>
</g>'''%dict(K=K,G=G,M=M)
def maskot(x,y,h): s=h/600; return f'<g transform="translate({x} {y}) scale({s})">{MASKOT}</g>'
# Greek-key (meander) band pattern, unit u (mm)
def meander_defs(u):
    p=f'M0 {u*.15} H{u*.85} V{u*.85} H{u*.3} V{u*.45} H{u*.6} V{u*.6}'
    return f'''<pattern id="mk" width="{u}" height="{u}" patternUnits="userSpaceOnUse">
<path d="{p}" fill="none" stroke="{Au}" stroke-width="{u*.09}" stroke-linecap="square"/></pattern>'''
def frame(W,H,b,inset,u):
    # band of meander with thin lines, inset from trim
    x0,y0=b+inset,b+inset; w,h=W-2*inset,H-2*inset
    s=f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="{Au}" stroke-width="{u*.09}"/>'
    s+=f'<rect x="{x0+u*1.3}" y="{y0+u*1.3}" width="{w-u*2.6}" height="{h-u*2.6}" fill="none" stroke="{Au}" stroke-width="{u*.09}"/>'
    # meander strips top/bottom/left/right
    s+=f'<rect x="{x0+u*.15}" y="{y0+u*.15}" width="{w-u*.3}" height="{u}" fill="url(#mk)"/>'
    s+=f'<rect x="{x0+u*.15}" y="{y0+h-u*1.15}" width="{w-u*.3}" height="{u}" fill="url(#mk)"/>'
    s+=f'<rect x="{x0+u*.15}" y="{y0+u*1.15}" width="{u}" height="{h-u*2.3}" fill="url(#mk)"/>'
    s+=f'<rect x="{x0+w-u*1.15}" y="{y0+u*1.15}" width="{u}" height="{h-u*2.3}" fill="url(#mk)"/>'
    return s
def stamp(x,y,s):
    return f'<g transform="translate({x} {y})"><rect width="{s}" height="{s}" rx="{s*.08}" fill="{R}"/><rect x="{s*.08}" y="{s*.08}" width="{s*.84}" height="{s*.84}" rx="{s*.05}" fill="none" stroke="{K}" stroke-width="{s*.035}"/><text x="{s/2}" y="{s*.73}" text-anchor="middle" font-family="Cha" font-weight="700" font-size="{s*.62}" fill="{K}">茶</text></g>'
def arrow(cx,y,s,col=Au):
    return f'<path d="M{cx-s*.5} {y} L{cx+s*.5} {y} L{cx} {y+s*.62} Z" fill="{col}"/>'
def T(x,y,txt,fs,fam='Oswald',w=700,fill=K,anc='middle',ls=0,style=''):
    return f'<text x="{x}" y="{y}" text-anchor="{anc}" font-family="{fam}" font-weight="{w}" font-size="{fs}" fill="{fill}" letter-spacing="{ls}" {style}>{txt}</text>'
B=20 # bleed mm
def doc(W,H,body,u,trim=False):
    TW,TH=W+2*B,H+2*B
    t=f'<rect x="{B}" y="{B}" width="{W}" height="{H}" fill="none" stroke="#ff00ff" stroke-width="2" stroke-dasharray="12 8"/>' if trim else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css">
<style>@page{{size:{TW}mm {TH}mm;margin:0}}html,body{{margin:0;padding:0}}svg{{display:block;width:{TW}mm;height:{TH}mm}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TW} {TH}"><defs>{meander_defs(u)}</defs>
<rect width="{TW}" height="{TH}" fill="{G}"/>{body}{t}</svg></body></html>'''

# ===== A. Penutup utama 3200 x 900 =====
def utama():
    W,H,u=3200,900,46; b=B; s=frame(W,H,b,30,u)
    cy=b+H/2
    # zona kiri: AMBIL (x 0..640), kanan: PESAN (2560..3200)
    zl,zr=b+640,b+2560
    for x in (zl,zr): s+=f'<line x1="{x}" y1="{b+150}" x2="{x}" y2="{b+H-150}" stroke="{Au}" stroke-width="5"/>'
    def zone(cx,num,l1,l2):
        z=f'<circle cx="{cx}" cy="{b+215}" r="62" fill="none" stroke="{Au}" stroke-width="7"/>'+T(cx,b+243,num,82,fill=Au)
        z+=T(cx,b+455,l1,170)+T(cx,b+580,l2,96,w=500,fill=Au,ls=10)
        z+=arrow(cx,b+630,120)
        return z
    s+=zone(b+330,'3','AMBIL','PESANAN')
    s+=zone(b+2870,'1','PESAN','&amp; BAYAR')
    # tengah: logo + wordmark
    d=700; lx=b+700; s+=L(lx,cy-d/2,d)
    tx=b+1440+ (2540-1440)/2
    s+=T(tx+10,b+430,'TOKO TEH',300,ls=8)
    s+=T(tx,b+545,'TJAP DUA KOI',92,fam='Cinzel',fill=Au,ls=30)
    s+=f'<line x1="{tx-420}" y1="{b+598}" x2="{tx+420}" y2="{b+598}" stroke="{Au}" stroke-width="4"/>'
    s+=T(tx,b+690,'Sepasang koi, secangkir teh',78,fam='Playfair Display',fill=K,style='font-style="italic"')
    return doc(W,H,s,u),doc(W,H,s,u,True)

# ===== B. Penutup samping A 1400 x 900: janji brand + maskot =====
def sampingA():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    s+=maskot(b+90,b+140,640)
    cx=b+905
    s+=T(cx,b+350,'TEH KENTAL,',112,ls=2)
    s+=T(cx,b+500,'TEMAN KENTAL.',112,ls=2,fill=Au)
    s+=f'<line x1="{cx-300}" y1="{b+585}" x2="{cx+300}" y2="{b+585}" stroke="{Au}" stroke-width="4"/>'
    s+=T(cx,b+680,'Mampir dulu, yuk!',84,fam='Playfair Display',style='font-style="italic"')
    s+=stamp(b+W-200,b+125,64)
    return doc(W,H,s,u),doc(W,H,s,u,True)

# ===== C. Penutup samping B 1400 x 900: ojol / online =====
def sampingB():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    d=440; s+=L(b+120,b+H/2-d/2-20,d)
    cx=b+930
    s+=T(cx,b+300,'PESANAN',190,ls=6)
    s+=T(cx,b+480,'ONLINE',190,ls=6,fill=Au)
    s+=T(cx,b+600,'OJOL AMBIL DI SINI',74,w=500,ls=8)
    s+=arrow(cx,b+650,110)
    return doc(W,H,s,u),doc(W,H,s,u,True)

for name,fn in (('1-penutup-utama-320x90',utama),('2-penutup-samping-A-140x90',sampingA),('3-penutup-samping-B-140x90',sampingB)):
    a,p=fn(); open(name+'.html','w').write(a); open(name+'-trim.html','w').write(p)
