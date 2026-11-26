exec(open("gen11.py").read().rsplit("\nP={",1)[0])
def waves2(W,y0):
    g=''
    for k_,op in ((0,.75),(70,.5),(140,.35)): g+=f'<path d="M0 {y0+k_} '+''.join('q100 -36 200 0 t200 0 ' for _ in range(5))+f'" fill="none" stroke="{SAGE}" stroke-opacity="{op}" stroke-width="12" stroke-linecap="round"/>'
    return g
def emblem(cx,cy,r):
    i=uid()
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{Au}"/><circle cx="{cx}" cy="{cy}" r="{r*.94}" fill="{M}"/><circle cx="{cx}" cy="{cy}" r="{r*.66}" fill="none" stroke="{Au}" stroke-width="{r*.02}"/><circle cx="{cx}" cy="{cy}" r="{r*.9}" fill="none" stroke="{K}" stroke-width="{r*.012}"/>'
    rr=r*.75
    g+=f'<defs><path id="a{i}" d="M{cx-rr} {cy} A{rr} {rr} 0 0 1 {cx+rr} {cy}"/><path id="b{i}" d="M{cx-rr} {cy} A{rr} {rr} 0 0 0 {cx+rr} {cy}"/></defs>'
    g+=f'<text font-family="Oswald" font-weight="700" font-size="{r*.135}" fill="{K}" letter-spacing="{r*.025}" text-anchor="middle"><textPath href="#a{i}" startOffset="50%">TOKO TEH · TJAP DUA KOI</textPath></text>'
    g+=f'<text font-family="Cinzel" font-weight="700" font-size="{r*.13}" fill="{Au}" letter-spacing="{r*.06}" text-anchor="middle" dominant-baseline="hanging"><textPath href="#b{i}" startOffset="50%">SAMARINDA</textPath></text>'
    for a in (-1,1): g+=star(cx+a*rr,cy,r*.05).replace(f'fill="{Au}"',f'fill="{K}"')
    g+=T(cx,cy-r*.2,'EST.',r*.14,fam='Cinzel',fill=Au,ls=r*.04)+T(cx,cy+r*.2,'2025',r*.4,fill=K,ls=r*.02)
    g+=koi(cx-r*.05,cy+r*.42,r*.0011*r/ r*0+ r*.0011, rot=0) if False else ''
    g+=f'<line x1="{cx-r*.36}" y1="{cy+r*.3}" x2="{cx+r*.36}" y2="{cy+r*.3}" stroke="{Au}" stroke-width="{r*.015}"/>'
    g+=stamp(cx-r*.1,cy+r*.36,r*.2)
    return g
def sisiEmblem():
    W,H=2000,900; s=waves2(W,720)
    s+=lily(1700,800,90,True)+lily(1450,860,60)+lily(430,860,70)
    s+=koi(250,770,.6,rot=-6)+koi(1770,760,.5,rot=8,flip=True,pat=ORG)
    s+=emblem(1000,365,315)
    s+=lantern(250,0,.62)+lantern(1750,0,.62)
    return W,H,G,s
def sisiCha():
    W,H=2000,900; s=waves2(W,720)
    s+=lstring(60,1940,20,6,.42)
    s+=stamp(770,190,460)
    s+=lily(300,800,90,True)+lily(560,860,60)+lily(1560,860,70)
    s+=koi(1750,770,.6,rot=6,flip=True,pat=ORG)+koi(250,760,.5,rot=-8)
    return W,H,G,s
P={'2m-emblem-200x90':sisiEmblem,'2m-lampion-cha-200x90':sisiCha}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s)); open(f'p-{n}.html','w').write(wrapT(W,H,s))
def elev2(n):
    _,_,_,low=P[n](); _,_,_,st=strip2()
    EH=2300; g=f'<rect width="2000" height="{EH}" fill="{G}"/>'
    g+=f'<rect x="300" y="400" width="1400" height="1000" fill="#BCD9E3"/><text x="1000" y="920" text-anchor="middle" font-family="Inter" font-size="70" fill="#56655d">jendela ±140 cm</text>'
    g+=f'<g transform="translate(0 400)">{st}</g><g transform="translate(1700 400)">{st}</g><g transform="translate(0 1400)">{low}</g>'
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>body{{margin:0;background:#111}}svg{{display:block}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -80 2160 2460" width="700" height="797">{g}</svg></body></html>'
for n in P: open(f'e-{n}.html','w').write(elev2(n))
