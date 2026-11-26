exec(open('gen10.py').read().split("P={'4m-ruko")[0])
SAGE='#A9C2A6'; MUST='#D9B35F'
def glow(x,y,r): return ''   # tidak ada efek cahaya: stiker potong
def wrapT(W,H,inner):   # cetak: latar transparan
    TW,TH=W+2*B,H+2*B
    return f'''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css">
<style>@page{{size:{TW}mm {TH}mm;margin:0}}html,body{{margin:0;background:transparent}}svg{{display:block;width:{TW}mm;height:{TH}mm}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TW} {TH}"><g transform="translate({B} {B})">{inner}</g></svg></body></html>'''
def lstring(x0,x1,y,n,s):
    g=f'<path d="M{x0} {y} Q{(x0+x1)/2} {y+60} {x1} {y}" fill="none" stroke="{Au}" stroke-width="14" stroke-linecap="round"/>'
    for i in range(n):
        t=(i+.5)/n;px=x0+(x1-x0)*t;py=y+120*t*(1-t); g+=lantern(px,py,s)
    return g
def shop(x,base,w,h,wall,i):
    win=M; sh=G if wall!=G else SAGE
    g=f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" fill="{wall}"/>'
    g+=f'<rect x="{x-8}" y="{base-h-22}" width="{w+16}" height="26" fill="{K if wall!=K else Au}"/><path d="M{x+w*.3} {base-h-20} Q{x+w/2} {base-h-70} {x+w*.7} {base-h-20} Z" fill="{K if wall!=K else Au}"/>'
    for wx in (.16,.58):
        X=x+w*wx;Y=base-h+40;ww=w*.26;wh=h*.3
        g+=f'<path d="M{X} {Y+wh} V{Y+ww/2} A{ww/2} {ww/2} 0 0 1 {X+ww} {Y+ww/2} V{Y+wh} Z" fill="{win}"/>'
        g+=f'<rect x="{X-ww*.3}" y="{Y+ww*.3}" width="{ww*.28}" height="{wh-ww*.3}" fill="{sh}"/><rect x="{X+ww*1.02}" y="{Y+ww*.3}" width="{ww*.28}" height="{wh-ww*.3}" fill="{sh}"/>'
    sy=base-h*.5; g+=f'<rect x="{x+w*.12}" y="{sy}" width="{w*.76}" height="{h*.11}" fill="{M}" stroke="{Au}" stroke-width="5"/>'
    if i%2: g+=T(x+w/2,sy+h*.085,'茶',h*.08,fam='Cha',fill=Au)
    g+=f'<path d="M{x+w*.2} {base} V{base-h*.25} A{w*.3} {w*.22} 0 0 1 {x+w*.8} {base-h*.25} V{base} Z" fill="{M}"/>'
    return g
def skyline2(x0,x1,base):
    g='';x=x0;spec=[(250,250,G),(220,290,K),(270,240,SAGE),(230,300,G),(250,260,MUST),(220,280,K)];i=0
    while x<x1-160:
        w,h,c=spec[i%6];w=min(w,x1-x);g+=shop(x,base,w,h,c,i);x+=w+12;i+=1
    return g
def ruko():
    W,H=4000,900; s=wordmark(W/2,300,300)
    base=H-110
    for a,b_ in ((50,1520),(2480,3950)):
        s+=f'<rect x="{a-10}" y="{base}" width="{b_-a+20}" height="110" fill="{G}"/>'+skyline2(a,b_,base)
    s+=T(785,H-30,'TEH TARIK · BAGEL · WRAP',58,w=500,ls=8,fill=K)+T(3215,H-30,'@tokoteh.tjapduakoi',58,fam='Inter',w=600,fill=K)
    for a,b_ in ((60,1330),(2670,3940)): s+=lstring(a,b_,300,5,.36)
    return W,H,M,s
def kolam():
    W,H=4000,900; s=wordmark(W/2,300,300)
    wy=560; wave=f'M0 {wy} '+''.join('q100 -50 200 0 t200 0 ' for _ in range(10))+f'V{H} H0 Z'
    s+=f'<path d="{wave}" fill="{G}"/>'
    s+=f'<path d="M0 {wy+80} '+''.join('q100 -40 200 0 t200 0 ' for _ in range(10))+f'" fill="none" stroke="{SAGE}" stroke-opacity=".6" stroke-width="10"/>'
    for r in (500,620,740): s+=f'<path d="M{W/2-r} {H} A{r} {r*.55} 0 0 1 {W/2+r} {H}" fill="none" stroke="{K}" stroke-opacity=".5" stroke-width="10"/>'
    s+=lily(250,660,110,True)+lily(1500,830,90)+lily(2560,840,80,True)+lily(3780,670,110)
    s+=koi(1000,700,1.0,rot=-4)+koi(3000,700,1.0,rot=4,flip=True,pat=ORG)
    return W,H,M,s
def strip4(side):
    W,H=400,1000; s=lantern(200,0,1.2)
    if side=='L':
        for i,ch in enumerate('TEHTARIK'):
            y=455+i*68+(20 if i>=3 else 0); s+=T(W/2,y,ch,70,fill=K if i<3 else Au)
    else: s+=koi(200,560,.6,rot=-90,pat=ORG)+koi(200,840,.6,rot=-90,pat=R)
    return W,H,M,s
def tegel(y,W,h=70):
    g=''
    for i,x in enumerate(range(0,W,h)): g+=f'<rect x="{x}" y="{y}" width="{h}" height="{h}" fill="{K if i%2 else M}"/><circle cx="{x+h/2}" cy="{y+h/2}" r="{h*.2}" fill="{Au if i%2 else K}"/>'
    return g
def spotfoto():
    W,H=2000,900; s=tegel(H-70,W)+cup(760,80,480,720,True)
    s+=T(370,380,'FOTO',210,ls=6,fill=K)+T(370,580,'DULU,',210,ls=6,fill=Au)
    s+=T(1630,380,'BARU',210,ls=6,fill=K)+T(1630,580,'TARIK.',210,ls=6,fill=Au)
    s+=f'<rect x="1350" y="660" width="560" height="90" rx="45" fill="{K}"/>'+igicon(1380,675,60,G)+T(1660,725,'@tokoteh.tjapduakoi',44,fill=G)
    s+=lantern(110,0,.55)+lantern(1890,0,.55)+star(700,140,26)+star(1290,190,22)
    return W,H,G,s
def strip2():
    W,H=300,1000; s=lantern(150,0,1.1)+koi(150,545,.5,rot=-90,pat=ORG)+koi(150,825,.5,rot=-90,pat=R)
    return W,H,G,s
P={'4m-ruko-400x90':ruko,'4m-kolam-400x90':kolam,'strip-kiri-40x100':lambda:strip4('L'),'strip-kanan-40x100':lambda:strip4('R'),'2m-spot-foto-200x90':spotfoto,'strip-2m-30x100':strip2}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s,wheel_guide(W,H) if n.startswith('4m') else ''))
    open(f'p-{n}.html','w').write(wrapT(W,H,s))
stripL=P['strip-kiri-40x100'];stripR=P['strip-kanan-40x100']
src=open('gen9.py').read(); src=src[src.index('# ===== tampak'):]
exec(src)
