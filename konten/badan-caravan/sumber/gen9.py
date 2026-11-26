import io,contextlib
exec(open('gen8.py').read())
MD='#5E1620'  # marun gelap
def wrap(W,H,bg,inner,guide=''):
    TW,TH=W+2*B,H+2*B
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css">
<style>@page{{size:{TW}mm {TH}mm;margin:0}}html,body{{margin:0}}svg{{display:block;width:{TW}mm;height:{TH}mm}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TW} {TH}"><rect width="{TW}" height="{TH}" fill="{bg}"/><g transform="translate({B} {B})">{inner}{guide}</g></svg></body></html>'''
def wheel_guide(W,H):  # zona roda (perkiraan) hanya di pratinjau
    return f'<path d="M{W/2-450} {H} A450 450 0 0 1 {W/2+450} {H}" fill="#000" fill-opacity=".25" stroke="#ff00ff" stroke-width="6" stroke-dasharray="20 14"/>'+T(W/2,H-120,'ZONA RODA (perkiraan)',40,fam='Inter',w=600,fill='#ff66ff')
def wordmark(cx,y,fs=280):
    return T(cx,y,'TOKO TEH',fs,ls=10)+T(cx,y+fs*.36,'TJAP DUA KOI',fs*.27,fam='Cinzel',fill=Au,ls=fs*.09)
def house(x,base,w,h,fill,win):
    g=f'<path d="M{x} {base} V{base-h} L{x+w/2} {base-h-w*.22} L{x+w} {base-h} V{base} Z" fill="{fill}"/>'
    g+=f'<rect x="{x+w*.14}" y="{base-h*.72}" width="{w*.28}" height="{h*.34}" rx="{w*.13}" fill="{win}"/><rect x="{x+w*.58}" y="{base-h*.72}" width="{w*.28}" height="{h*.34}" rx="{w*.13}" fill="{win}"/>'
    g+=f'<rect x="{x+w*.36}" y="{base-h*.3}" width="{w*.28}" height="{h*.3}" fill="{win}"/>'
    return g
def skyline(x0,x1,base,col,win):
    g='';x=x0;spec=[(240,200),(200,250),(280,220),(220,260),(260,210),(210,240)];i=0
    while x<x1-150:
        w,h=spec[i%len(spec)];w=min(w,x1-x);g+=house(x,base,w,h,col,win);x+=w+10;i+=1
    return g
def lantern_string(x0,x1,y,n,s,col=R):
    g=f'<path d="M{x0} {y} Q{(x0+x1)/2} {y+60} {x1} {y}" fill="none" stroke="{Au}" stroke-width="6"/>'
    for i in range(n):
        t=(i+.5)/n;px=x0+(x1-x0)*t;py=y+120*t*(1-t)
        g+=lantern(px,py,s)
    return g
# ===== 4 m RUKO (400x90, latar marun) =====
def ruko():
    W,H=4000,900; s=''
    s+=wordmark(W/2,300,300)
    base=H-110
    for a,b_ in ((60,1500),(2500,3940)): s+=skyline(a,b_,base,G,'#7A1F2B')
    for a,b_ in ((60,1330),(2670,3940)): s+=lantern_string(a,b_,330,5,.36)
    s+=f'<rect x="0" y="{base}" width="{W}" height="110" fill="{G}"/>'
    s+=T(780,H-38,'TEH TARIK · BAGEL · WRAP',60,w=500,ls=8,fill=K)
    s+=T(3220,H-38,'@tokoteh.tjapduakoi',60,fam='Inter',w=600,fill=K)
    s+=f'<line x1="0" y1="18" x2="{W}" y2="18" stroke="{Au}" stroke-width="8"/>'
    return W,H,M,s
# ===== 4 m KOLAM =====
def kolam():
    W,H=4000,900; s=''
    s+=wordmark(W/2,300,300)
    wy=560; wave=f'M0 {wy} '+''.join(f'q100 -50 200 0 t200 0 ' for _ in range(10))+f'V{H} H0 Z'
    s+=f'<path d="{wave}" fill="{G}"/>'
    s+=f'<path d="M0 {wy+70} '+''.join('q100 -40 200 0 t200 0 ' for _ in range(10))+'" fill="none" stroke="#2F6B4F" stroke-width="10"/>'
    for r in (500,620,740): s+=f'<path d="M{W/2-r} {H} A{r} {r*.55} 0 0 1 {W/2+r} {H}" fill="none" stroke="{K}" stroke-opacity=".45" stroke-width="10"/>'
    s+=koi(1000,700,1.05,rot=-4)+koi(3000,700,1.05,rot=4,flip=True,pat=ORG)
    for x,y,r in ((1350,620,16),(1400,570,11),(2650,610,15),(2600,560,10)): s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{K}" stroke-width="6"/>'
    s+=f'<line x1="0" y1="18" x2="{W}" y2="18" stroke="{Au}" stroke-width="8"/>'
    return W,H,M,s
# ===== strip 40 x 100 =====
def stripL():
    W,H=400,1000; s=stamp(100,40,200)
    for i,ch in enumerate('TEHTARIK'):
        y=340+i*82+(30 if i>=3 else 0); s+=T(W/2,y,ch,82,fill=K if i<3 else Au)
    return W,H,M,s
def stripR():
    W,H=400,1000; s=stamp(100,40,200)
    s+=f'<path d="M200 300 C120 450 280 600 200 760 C140 880 220 960 200 990" fill="none" stroke="{K}" stroke-opacity=".35" stroke-width="8" stroke-dasharray="4 18" stroke-linecap="round"/>'
    s+=koi(200,450,.42,rot=-90)+koi(200,780,.42,rot=-90,pat=ORG)
    return W,H,M,s
# ===== 2 m spot foto =====
def spotfoto():
    W,H=2000,900; s=''
    s+=cup(760,90,480,740,True)
    s+=T(370,400,'FOTO',210,ls=6)+T(370,600,'DULU,',210,ls=6)
    s+=T(1630,400,'BARU',210,ls=6,fill=Au)+T(1630,600,'TARIK.',210,ls=6,fill=Au)
    s+=f'<rect x="1350" y="700" width="560" height="90" rx="45" fill="{K}"/>'+igicon(1380,715,60,G)+T(1660,765,'@tokoteh.tjapduakoi',44,fill=G)
    s+=cloud(90,800,.9)+star(720,140,30)+star(1290,200,22)
    return W,H,G,s
# ===== 2 m jendela ojol =====
def ojol():
    W,H=2000,900; s=''
    s+=maskot(80,120,700)
    s+=T(1010,300,'PESANAN',190,ls=6)+T(1010,490,'ONLINE',190,ls=6,fill=Au)
    s+=T(1010,600,'OJOL AMBIL DI JENDELA INI',58,w=500,ls=6)
    s+=f'<path d="M960 720 L1060 720 L1010 650 Z" fill="{Au}"/>'
    s+=f'<rect x="1500" y="560" width="300" height="300" rx="16" fill="{K}"/>'+qr2(1520,580,260,'https://www.instagram.com/tokoteh.tjapduakoi/')
    s+=T(1650,550,'Follow kami',44,fam='Playfair Display',style='font-style="italic"')
    return W,H,G,s
P={'4m-ruko-400x90':ruko,'4m-kolam-400x90':kolam,'strip-kiri-40x100':stripL,'strip-kanan-40x100':stripR,'2m-spot-foto-200x90':spotfoto,'2m-ojol-200x90':ojol}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s,wheel_guide(W,H) if n.startswith('4m') else ''))
    open(f'p-{n}.html','w').write(wrap(W,H,bg,s))
# ===== tampak 4 m (elevasi) =====
def elev(lower):
    W,H,bg,low=P[lower](); _,_,_,sl=stripL(); _,_,_,sr=stripR()
    EH=2300; g=f'<rect width="4000" height="{EH}" fill="{M}"/><rect width="4000" height="100" fill="{G}"/>'
    g+=f'<rect x="400" y="300" width="3200" height="1100" fill="#BCD9E3"/><text x="2000" y="900" text-anchor="middle" font-family="Inter" font-size="90" fill="#56655d">jendela 320 cm (penutup terbuka ke atas)</text>'
    g+=f'<g transform="translate(0 400)">{sl}</g><g transform="translate(3600 400)">{sr}</g>'
    g+=f'<g transform="translate(0 1400)">{low}</g>'
    g+=f'<circle cx="2000" cy="{EH+60}" r="330" fill="#1a1a1a"/><circle cx="2000" cy="{EH+60}" r="140" fill="#9a948a"/>'
    g+=f'<text x="2000" y="{EH+520}" text-anchor="middle" font-family="Inter" font-size="80" fill="#ccc">roda (posisi & ukuran perkiraan)</text>'
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>body{{margin:0;background:#111}}svg{{display:block}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="-100 -100 4200 3050" width="1400" height="1017">{g}</svg></body></html>'
open('e-ruko.html','w').write(elev('4m-ruko-400x90')); open('e-kolam.html','w').write(elev('4m-kolam-400x90'))
