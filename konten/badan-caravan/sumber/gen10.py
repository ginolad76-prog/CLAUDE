exec(open('gen9.py').read().split('P={')[0])
MINT='#8FC9A8';BUT='#F2CF6E';TERA='#D9774B';TEAL='#3E8E8B';PINK='#EBA3A3';SKY='#2F8F7F';LILY='#5FAF5A';LOTUS='#F29BB0';DARK='#3A1A1E'
GLOW=f'<defs><radialGradient id="glow"><stop offset="0" stop-color="{BUT}" stop-opacity=".75"/><stop offset="1" stop-color="{BUT}" stop-opacity="0"/></radialGradient><linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY}"/><stop offset="1" stop-color="{G}"/></linearGradient></defs>'
def glow(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#glow)"/>'
def lstring(x0,x1,y,n,s):
    g=f'<path d="M{x0} {y} Q{(x0+x1)/2} {y+60} {x1} {y}" fill="none" stroke="{Au}" stroke-width="6"/>'
    for i in range(n):
        t=(i+.5)/n;px=x0+(x1-x0)*t;py=y+120*t*(1-t); g+=glow(px,py+140*s,170*s)+lantern(px,py,s)
    return g
def shop(x,base,w,h,wall,i):
    g=f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" fill="{wall}"/>'
    g+=f'<rect x="{x-8}" y="{base-h-22}" width="{w+16}" height="26" fill="{K}"/><path d="M{x+w*.3} {base-h-22} Q{x+w/2} {base-h-70} {x+w*.7} {base-h-22} Z" fill="{K}"/>'
    for wx in (.16,.58):
        X=x+w*wx;Y=base-h+40;ww=w*.26;wh=h*.3
        g+=f'<path d="M{X} {Y+wh} V{Y+ww/2} A{ww/2} {ww/2} 0 0 1 {X+ww} {Y+ww/2} V{Y+wh} Z" fill="{BUT if i%2 else "#FBE3A6"}"/>'
        g+=f'<rect x="{X-ww*.32}" y="{Y+ww*.3}" width="{ww*.3}" height="{wh-ww*.3}" fill="{G}"/><rect x="{X+ww*1.02}" y="{Y+ww*.3}" width="{ww*.3}" height="{wh-ww*.3}" fill="{G}"/>'
    sy=base-h*.5; g+=f'<rect x="{x+w*.12}" y="{sy}" width="{w*.76}" height="{h*.11}" fill="{R if i%3 else G}" stroke="{Au}" stroke-width="5"/>'
    g+=T(x+w/2,sy+h*.085,'茶' if i%2 else '★',h*.08,fam='Cha',fill=Au)
    g+=f'<path d="M{x+w*.2} {base} V{base-h*.25} A{w*.3} {w*.22} 0 0 1 {x+w*.8} {base-h*.25} V{base} Z" fill="{DARK}"/>'
    g+=glow(x+w/2,base-h*.12,w*.28)
    return g
def skyline2(x0,x1,base):
    g='';x=x0;spec=[(250,250,MINT),(220,290,BUT),(270,240,TERA),(230,300,TEAL),(250,260,PINK),(220,280,K)];i=0
    while x<x1-160:
        w,h,c=spec[i%6];w=min(w,x1-x);g+=shop(x,base,w,h,c,i);x+=w+12;i+=1
    return g
def ruko():
    W,H=4000,900; s=GLOW
    s+=wordmark(W/2,300,300)
    base=H-110
    for a,b_ in ((50,1520),(2480,3950)): s+=skyline2(a,b_,base)
    for a,b_ in ((60,1330),(2670,3940)): s+=lstring(a,b_,300,5,.36)
    s+=f'<rect x="0" y="{base}" width="{W}" height="110" fill="{G}"/>'
    s+=''.join(f'<rect x="{x}" y="{base}" width="40" height="14" fill="{Au}"/>' for x in range(0,W,80))
    s+=T(780,H-30,'TEH TARIK · BAGEL · WRAP',60,w=500,ls=8,fill=K)+T(3220,H-30,'@tokoteh.tjapduakoi',60,fam='Inter',w=600,fill=K)
    s+=f'<line x1="0" y1="18" x2="{W}" y2="18" stroke="{Au}" stroke-width="8"/>'
    return W,H,M,s
def lily(x,y,r,flower=False):
    import math
    ry=r*.45; a=math.radians(14)
    g=f'<path d="M{x} {y} L{x+r*math.cos(a):.1f} {y-ry*math.sin(a):.1f} A{r} {ry} 0 1 0 {x+r*math.cos(a):.1f} {y+ry*math.sin(a):.1f} Z" fill="{LILY}"/><path d="M{x} {y} L{x-r*.8} {y}" stroke="#3F8A3D" stroke-width="4" stroke-opacity=".6"/>'
    if flower:
        for a in (-40,-15,15,40): g+=f'<ellipse cx="{x}" cy="{y-r*.35}" rx="{r*.16}" ry="{r*.42}" fill="{LOTUS}" transform="rotate({a} {x} {y-r*.05})"/>'
        g+=f'<circle cx="{x}" cy="{y-r*.15}" r="{r*.12}" fill="{BUT}"/>'
    return g
def kolam():
    W,H=4000,900; s=GLOW
    s+=wordmark(W/2,300,300)
    for x in (300,3700): s+=lstring(x-220,x+220,40,2,.32)
    wy=520; wave=f'M0 {wy} '+''.join('q100 -50 200 0 t200 0 ' for _ in range(10))+f'V{H} H0 Z'
    s+=f'<path d="{wave}" fill="url(#water)"/>'
    for k_,op in ((70,.5),(170,.3)): s+=f'<path d="M0 {wy+k_} '+''.join('q100 -40 200 0 t200 0 ' for _ in range(10))+f'" fill="none" stroke="{K}" stroke-opacity="{op}" stroke-width="8"/>'
    for r in (500,620,740): s+=f'<path d="M{W/2-r} {H} A{r} {r*.55} 0 0 1 {W/2+r} {H}" fill="none" stroke="{K}" stroke-opacity=".55" stroke-width="10"/>'
    s+=lily(250,640,110,True)+lily(1500,820,90)+lily(2550,830,80,True)+lily(3800,650,110)+lily(3350,830,70)+lily(620,840,70)
    s+=koi(1000,690,1.0,rot=-4)+koi(3000,690,1.0,rot=4,flip=True,pat=ORG)
    s+=koi(1450,600,.45,rot=10,pat=Au)+koi(2600,600,.45,rot=-10,flip=True,pat=R)
    s+=f'<line x1="0" y1="18" x2="{W}" y2="18" stroke="{Au}" stroke-width="8"/>'
    return W,H,M,s
def strip4(side):
    W,H=400,1000; s=GLOW+glow(200,150,190)+lantern(200,10,.8)
    if side=='L':
        for i,ch in enumerate('TEHTARIK'):
            y=430+i*70+(24 if i>=3 else 0); s+=T(W/2,y,ch,70,fill=K if i<3 else BUT)
    else:
        s+=koi(200,520,.4,rot=-90,pat=ORG)+koi(200,820,.4,rot=-90,pat=R)+lily(120,960,60,True)
    return W,H,M,s
def tegel(y,W,h=70):
    g=''
    for i,x in enumerate(range(0,W,h)):
        g+=f'<rect x="{x}" y="{y}" width="{h}" height="{h}" fill="{K if i%2 else TEAL}"/><circle cx="{x+h/2}" cy="{y+h/2}" r="{h*.22}" fill="{R if i%2 else BUT}"/>'
    return g
def spotfoto():
    W,H=2000,900; s=GLOW
    s+=tegel(H-70,W)
    s+=glow(1000,460,520)+cup(760,80,480,720,True)
    s+=T(370,380,'FOTO',210,ls=6,fill=K)+T(370,580,'DULU,',210,ls=6,fill=BUT)
    s+=T(1630,380,'BARU',210,ls=6,fill=K)+T(1630,580,'TARIK.',210,ls=6,fill=BUT)
    s+=f'<rect x="1350" y="660" width="560" height="90" rx="45" fill="{K}"/>'+igicon(1380,675,60,G)+T(1660,725,'@tokoteh.tjapduakoi',44,fill=G)
    s+=lantern(110,0,.55)+lantern(1890,0,.55)
    for x,y,c in ((700,130,BUT),(1290,190,PINK),(640,620,MINT),(1330,560,BUT),(260,660,PINK)): s+=star(x,y,26).replace(f'fill="{Au}"',f'fill="{c}"')
    return W,H,G,s
def ojol():
    W,H=2000,900; s=GLOW
    s+=tegel(H-70,W)
    s+=glow(380,440,380)+maskot(80,80,690)
    s+=T(1010,280,'PESANAN',190,ls=6,fill=K)+T(1010,470,'ONLINE',190,ls=6,fill=BUT)
    s+=f'<rect x="690" y="520" width="640" height="80" rx="40" fill="{R}"/>'+T(1010,575,'OJOL AMBIL DI JENDELA INI',46,w=500,ls=4,fill=K)
    s+=f'<path d="M960 720 L1060 720 L1010 650 Z" fill="{BUT}"/>'
    s+=f'<rect x="1500" y="520" width="300" height="300" rx="16" fill="{K}"/>'+qr2(1520,540,260,'https://www.instagram.com/tokoteh.tjapduakoi/')
    s+=T(1650,505,'Follow kami',44,fam='Playfair Display',fill=K,style='font-style="italic"')
    s+=lantern(1890,0,.5)
    return W,H,G,s
def strip2():
    W,H=300,1000; s=GLOW+glow(150,150,150)+lantern(150,10,.62)
    s+=koi(150,560,.32,rot=-90,pat=ORG)+koi(150,820,.32,rot=-90,pat=R)
    s+=f'<path d="M150 380 V1000" stroke="{K}" stroke-opacity=".25" stroke-width="6" stroke-dasharray="4 16" stroke-linecap="round"/>'
    return W,H,G,s
P={'4m-ruko-400x90':ruko,'4m-kolam-400x90':kolam,'strip-kiri-40x100':lambda:strip4('L'),'strip-kanan-40x100':lambda:strip4('R'),'2m-spot-foto-200x90':spotfoto,'2m-ojol-200x90':ojol,'strip-2m-30x100':strip2}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s,wheel_guide(W,H) if n.startswith('4m') else ''))
    open(f'p-{n}.html','w').write(wrap(W,H,bg,s))
stripL=P['strip-kiri-40x100'];stripR=P['strip-kanan-40x100']
src=open('gen9.py').read(); src=src[src.index('# ===== tampak'):]
src=src.replace("g=f'<rect width=\"4000\" height=\"{EH}\" fill=\"{M}\"/>","g=GLOW+f'<rect width=\"4000\" height=\"{EH}\" fill=\"{M}\"/>")
exec(src)
