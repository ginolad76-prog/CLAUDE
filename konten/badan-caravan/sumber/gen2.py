src=open('gen.py').read(); exec(src[:src.index('# ===== A.')])
GD='#0A3A26'; RIP='#2F6B4F'; TEA='#B9824F'; TEA2='#8A5A30'; FOAM='#EAD9B8'; ORG='#D9602A'
_id=[0]
def uid(): _id[0]+=1; return f'c{_id[0]}'
BODY="M170 0 C150 -60 40 -85 -60 -55 C-120 -38 -160 -15 -185 0 C-160 15 -120 38 -60 55 C40 85 150 60 170 0 Z"
def koi(x,y,s,rot=0,flip=False,pat=R):
    i=uid(); fx=-1 if flip else 1
    g=f'<g transform="translate({x} {y}) rotate({rot}) scale({s*fx} {s})"><clipPath id="{i}"><path d="{BODY}"/></clipPath>'
    st=f'stroke="{Au}" stroke-width="7" stroke-linejoin="round"'
    g+=f'<path d="M-170 0 C-230 -70 -300 -95 -335 -62 C-300 -32 -282 -12 -270 0 C-282 12 -300 32 -335 62 C-300 95 -230 70 -170 0 Z" fill="{K}" {st}/>'
    g+=f'<path d="M-200 -30 L-300 -60 M-205 0 L-290 0 M-200 30 L-300 60" stroke="{Au}" stroke-width="4" fill="none"/>'
    g+=f'<path d="M30 -72 C0 -125 -90 -110 -115 -48 Z" fill="{K}" {st}/>'
    g+=f'<path d="M70 48 C55 115 5 125 -12 102 C8 82 28 62 42 48 Z" fill="{K}" {st}/>'
    g+=f'<path d="{BODY}" fill="{K}" {st}/>'
    g+=f'<g clip-path="url(#{i})"><ellipse cx="95" cy="-45" rx="55" ry="30" fill="{pat}"/><ellipse cx="-40" cy="20" rx="70" ry="38" fill="{pat}"/><ellipse cx="-140" cy="-25" rx="35" ry="22" fill="{pat}"/></g>'
    g+=f'<path d="{BODY}" fill="none" {st}/>'
    g+=f'<circle cx="122" cy="-14" r="13" fill="{G}"/><circle cx="126" cy="-18" r="4" fill="#fff"/>'
    g+=f'<path d="M140 22 Q152 30 164 20" stroke="{G}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    g+=f'<path d="M160 10 Q190 25 200 55" stroke="{Au}" stroke-width="4" fill="none"/>'
    return g+'</g>'
def ripples(cx,cy,w,n=3,col=RIP):
    return ''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{w*(k+1)/n/2}" ry="{w*(k+1)/n/9}" fill="none" stroke="{col}" stroke-width="6"/>' for k in range(n))
def glass(x,y,w,h,steam=True,inner=''):
    """x,y top-left of glass"""
    i=uid(); bw=w*.78; o=(w-bw)/2
    p=f'M{x} {y} L{x+w} {y} L{x+w-o} {y+h} L{x+o} {y+h} Z'
    g=f'<clipPath id="{i}"><path d="{p}"/></clipPath><defs><linearGradient id="t{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{TEA}"/><stop offset="1" stop-color="{TEA2}"/></linearGradient></defs>'
    g+=f'<g clip-path="url(#{i})"><rect x="{x}" y="{y+h*.1}" width="{w}" height="{h}" fill="url(#t{i})"/><rect x="{x}" y="{y+h*.1}" width="{w}" height="{h*.12}" fill="{FOAM}"/>{inner}</g>'
    g+=f'<path d="{p}" fill="none" stroke="{K}" stroke-width="{w*.035}" stroke-linejoin="round"/>'
    g+=f'<path d="M{x+w*.12} {y+h*.28} L{x+w*.17} {y+h*.85}" stroke="#fff" stroke-opacity=".45" stroke-width="{w*.035}" stroke-linecap="round"/>'
    if steam:
        for k,dx in enumerate((.3,.5,.7)):
            sx=x+w*dx; g+=f'<path d="M{sx} {y-h*.06} c{-w*.08} {-h*.1} {w*.08} {-h*.15} 0 {-h*.26}" fill="none" stroke="{K}" stroke-opacity=".8" stroke-width="{w*.03}" stroke-linecap="round"/>'
    return g
def lantern(x,y,s):
    g=f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+40*s}" stroke="{Au}" stroke-width="{4*s}"/>'
    g+=f'<rect x="{x-35*s}" y="{y+40*s}" width="{70*s}" height="{22*s}" rx="{4*s}" fill="{Au}"/>'
    g+=f'<ellipse cx="{x}" cy="{y+140*s}" rx="{85*s}" ry="{92*s}" fill="{R}"/>'
    for dx in (-50,-20,20,50): g+=f'<path d="M{x+dx*s*.3} {y+55*s} Q{x+dx*s*1.25} {y+140*s} {x+dx*s*.3} {y+225*s}" fill="none" stroke="#8E1C17" stroke-width="{4*s}"/>'
    g+=f'<ellipse cx="{x-28*s}" cy="{y+110*s}" rx="{16*s}" ry="{34*s}" fill="#fff" fill-opacity=".18"/>'
    g+=f'<rect x="{x-35*s}" y="{y+218*s}" width="{70*s}" height="{22*s}" rx="{4*s}" fill="{Au}"/>'
    g+=f'<text x="{x}" y="{y+165*s}" text-anchor="middle" font-family="Cha" font-size="{70*s}" fill="{Au}">茶</text>'
    for dx in (-14,-5,5,14): g+=f'<line x1="{x+dx*s}" y1="{y+240*s}" x2="{x+dx*s}" y2="{y+320*s}" stroke="{Au}" stroke-width="{4*s}"/>'
    return g
def cloud(x,y,s,flip=False):
    f=-1 if flip else 1
    return f'<g transform="translate({x} {y}) scale({s*f} {s})" fill="none" stroke="{Au}" stroke-width="6" stroke-linecap="round"><path d="M0 0 H220 M30 0 a40 40 0 1 1 70 -30 a45 45 0 1 1 85 15 a30 30 0 1 1 30 15"/><path d="M60 -10 a14 14 0 1 1 18 -14"/><path d="M150 -20 a16 16 0 1 1 22 -12"/></g>'
def panel(x,y,w,h,cap,body,capfs=52):
    i=uid()
    g=f'<clipPath id="{i}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22"/></clipPath>'
    g+=f'<g clip-path="url(#{i})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{GD}"/>{body}</g>'
    g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="none" stroke="{K}" stroke-width="9"/>'
    g+=T(x+w/2,y+h+95,cap,capfs,ls=2)
    return g
def num(x,y,n): return f'<circle cx="{x}" cy="{y}" r="34" fill="{Au}"/>'+T(x,y+16,n,46,fill=G)

# ===== UTAMA =====
def utama():
    W,H,u=3200,900,46; b=B; s=frame(W,H,b,30,u)
    top=b+30+u*1.3
    s+=lantern(b+260,top,1.25)+lantern(b+2940,top,1.25)
    s+=cloud(b+150,b+H-150,1.1)+cloud(b+3050,b+H-150,1.1,True)
    d=790; s+=L(b+450,b+H/2-d/2,d)
    tx=b+2050
    s+=T(tx,b+445,'TOKO TEH',370,ls=10)
    s+=T(tx,b+570,'TJAP DUA KOI',100,fam='Cinzel',fill=Au,ls=34)
    s+=f'<line x1="{tx-480}" y1="{b+618}" x2="{tx+480}" y2="{b+618}" stroke="{Au}" stroke-width="5"/>'
    s+=T(tx,b+720,'Sepasang koi, segelas teh',92,fam='Playfair Display',style='font-style="italic"')
    return doc(W,H,s,u)

# ===== KOMIK =====
PW,PH=360,520
def komikA():
    W,H,u=1400,900,30; b=B; s=frame(W,H,b,24,u); y=b+110; xs=[b+95+k*(PW+45) for k in range(3)]
    # 1 sendirian
    x=xs[0]; body=ripples(x+180,y+400,300)+ripples(x+90,y+150,120,2)+koi(x+175,y+330,.42,rot=-8)
    body+=f'<circle cx="{x+300}" cy="{y+250}" r="10" fill="none" stroke="{K}" stroke-width="4"/><circle cx="{x+318}" cy="{y+210}" r="7" fill="none" stroke="{K}" stroke-width="4"/>'
    s+=panel(x,y,PW,PH,'Sendirian…',body)+num(x+30,y+30,'1')
    # 2 wangi teh
    x=xs[1]; body=f'<rect x="{x}" y="{y}" width="{PW}" height="{PH*.42}" fill="#16573C"/>'+glass(x+120,y+40,120,150)
    body+=ripples(x+180,y+PH*.42+20,320,2)+koi(x+165,y+390,.42,rot=-35)
    body+=T(x+290,y+330,'!',120,fill=Au)
    for k in range(3): body+=f'<path d="M{x+150+k*30} {y+200} q-20 40 0 80 q20 40 0 80" fill="none" stroke="{K}" stroke-opacity=".7" stroke-width="5" stroke-dasharray="10 12"/>'
    s+=panel(x,y,PW,PH,'Wangi apa ini?',body)+num(x+30,y+30,'2')
    # 3 lompat
    x=xs[2]; body=f'<rect x="{x}" y="{y+PH*.68}" width="{PW}" height="{PH}" fill="#0C3322"/><path d="M{x} {y+PH*.68} q45 -18 90 0 t90 0 t90 0 t90 0" fill="none" stroke="{K}" stroke-width="5"/>'
    body+=koi(x+190,y+220,.42,rot=-50)
    body+=f'<path d="M{x+80} {y+PH*.68} q20 -60 40 -10 M{x+230} {y+PH*.68} q25 -70 45 -5" fill="none" stroke="{K}" stroke-width="7" stroke-linecap="round"/>'
    for cx,cy,r in ((x+90,y+300,10),(x+120,y+260,8),(x+260,y+300,9),(x+290,y+270,7)): body+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{K}"/>'
    body+=f'<path d="M{x+100} {y+420} q90 -330 210 -330" fill="none" stroke="{Au}" stroke-width="5" stroke-dasharray="14 12"/>'
    s+=panel(x,y,PW,PH,'Hup!',body)+num(x+30,y+30,'3')
    return doc(W,H,s,u)
def komikB():
    W,H,u=1400,900,30; b=B; s=frame(W,H,b,24,u); y=b+110; xs=[b+95+k*(PW+45) for k in range(3)]
    # 4 koi kedua
    x=xs[0]; body=f'<rect x="{x}" y="{y+PH*.68}" width="{PW}" height="{PH}" fill="#0C3322"/><path d="M{x} {y+PH*.68} q45 -18 90 0 t90 0 t90 0 t90 0" fill="none" stroke="{K}" stroke-width="5"/>'
    body+=koi(x+170,y+230,.42,rot=50,flip=True,pat=ORG)
    for cx,cy,r in ((x+80,y+300,9),(x+280,y+290,10),(x+250,y+250,7)): body+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{K}"/>'
    s+=panel(x,y,PW,PH,'Eh, kamu juga?',body)+num(x+30,y+30,'4')
    # 5 ketemu di segelas teh
    x=xs[1]; inner=koi(x+150,y+290,.25,rot=-20)+koi(x+215,y+390,.25,rot=160,pat=ORG)
    body=glass(x+60,y+120,240,360,False,inner)
    body+=f'<path d="M{x+180} {y+60} c-30 -30 -60 0 -30 25 l30 25 l30 -25 c30 -25 0 -55 -30 -25 z" fill="{R}"/>'
    s+=panel(x,y,PW,PH,'Ketemu di sini.',body)+num(x+30,y+30,'5')
    # 6 penutup logo
    x=xs[2]; body=L(x+40,y+40,280)+T(x+180,y+400,'Sepasang koi,',50,fam='Playfair Display',style='font-style="italic"')+T(x+180,y+465,'segelas teh.',50,fam='Playfair Display',fill=Au,style='font-style="italic"')
    s+=panel(x,y,PW,PH,'Tjap Dua Koi',body)+num(x+30,y+30,'6')
    return doc(W,H,s,u)

# ===== ALTERNATIF (ide 1+3+5) =====
def altA():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    s+=glass(b+190,b+470,230,300,False)
    for k,dx in enumerate((.3,.5,.7)):
        sx=b+190+230*dx; s+=f'<path d="M{sx} {b+450} c-25 -40 25 -60 0 -100" fill="none" stroke="{K}" stroke-opacity=".85" stroke-width="9" stroke-linecap="round"/>'
    s+=f'<path d="M{b+305} {b+340} c-60 -40 -10 -90 30 -110" fill="none" stroke="{K}" stroke-opacity=".6" stroke-width="7" stroke-dasharray="4 14" stroke-linecap="round"/>'
    s+=koi(b+390,b+220,.5,rot=-20)
    s+=T(b+925,b+420,'Sepasang koi,',112,fam='Playfair Display',style='font-style="italic"')
    s+=f'<line x1="{b+700}" y1="{b+500}" x2="{b+1140}" y2="{b+500}" stroke="{Au}" stroke-width="4"/>'
    s+=T(b+920,b+610,'TARIK NAPAS, TARIK TEH.',62,w=500,fill=Au,ls=4)
    return doc(W,H,s,u)
def altB():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    s+=ripples(b+1030,b+470,520,3)
    s+=koi(b+1030,b+440,.62,rot=10,flip=True,pat=ORG)
    s+=T(b+470,b+420,'segelas teh.',125,fam='Playfair Display',fill=Au,style='font-style="italic"')
    s+=f'<line x1="{b+250}" y1="{b+500}" x2="{b+690}" y2="{b+500}" stroke="{Au}" stroke-width="4"/>'
    s+=T(b+470,b+590,'HIDUP SUDAH BERAT,',58,w=500,ls=4)+T(b+470,b+670,'TEHNYA JANGAN.',58,w=500,ls=4)
    return doc(W,H,s,u)
for n,f in (('1-penutup-utama-320x90',utama),('2A-komik-140x90',komikA),('3B-komik-140x90',komikB),('2A-alternatif-140x90',altA),('3B-alternatif-140x90',altB)):
    open(n+'.html','w').write(f())
