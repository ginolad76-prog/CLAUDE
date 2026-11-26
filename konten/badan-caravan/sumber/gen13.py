exec(open("gen12.py").read().split("P={'2m-emblem")[0])
WOOD='#A9754B'; WOODD='#7E5435'
def sisiA():
    W,H=2000,900; s=waves2(W,730)
    s+=lstring(60,690,20,3,.42)+lstring(1310,1940,20,3,.42)
    s+=emblem(1000,385,300)
    s+=lily(1700,810,90,True)+lily(1450,865,60)+lily(430,865,70)
    s+=koi(250,780,.6,rot=-6)+koi(1770,770,.5,rot=8,flip=True,pat=ORG)
    return W,H,G,s
def jar(x,base,w,h,lid,label,fill):
    g=f'<rect x="{x}" y="{base-h}" width="{w}" height="{h}" rx="{w*.12}" fill="#DCE6E2" fill-opacity=".9" stroke="{K}" stroke-width="5"/>'
    g+=f'<rect x="{x+w*.08}" y="{base-h*.62}" width="{w*.84}" height="{h*.55}" rx="{w*.08}" fill="{fill}"/>'
    g+=f'<rect x="{x-w*.04}" y="{base-h-h*.13}" width="{w*1.08}" height="{h*.15}" rx="{w*.05}" fill="{lid}"/><rect x="{x+w*.35}" y="{base-h-h*.2}" width="{w*.3}" height="{h*.08}" rx="6" fill="{lid}"/>'
    g+=f'<rect x="{x+w*.12}" y="{base-h*.52}" width="{w*.76}" height="{h*.28}" fill="{K}" stroke="{Au}" stroke-width="4"/>'+T(x+w/2,base-h*.33,label,min(w*.17,h*.12),fill=G,ls=2)
    return g
def kettle(x,base,s):
    return f'<g transform="translate({x} {base}) scale({s})"><path d="M-70 0 Q-90 -100 0 -110 Q90 -100 70 0 Z" fill="#C9CDCC" stroke="{K}" stroke-width="6"/><path d="M60 -70 Q120 -90 130 -140" fill="none" stroke="#C9CDCC" stroke-width="16" stroke-linecap="round"/><path d="M-60 -80 Q-120 -60 -70 -20" fill="none" stroke="{K}" stroke-width="10"/><rect x="-25" y="-130" width="50" height="22" rx="8" fill="{G}"/></g>'
def sisiB():
    W,H=2000,900; s=waves2(W,740)
    # rak
    y=600; s+=f'<rect x="110" y="{y}" width="900" height="28" rx="6" fill="{WOOD}"/><rect x="150" y="{y+28}" width="24" height="50" fill="{WOODD}"/><rect x="946" y="{y+28}" width="24" height="50" fill="{WOODD}"/>'
    s+=jar(150,y,240,300,G,'TEH HITAM','#5A3A22')+jar(440,y,240,300,M,'MATCHA','#7FA650')+jar(730,y,240,300,Au,'HOUJICHA','#9A5A32')
    s+=T(1510,320,'Dua koi di kolam tenang,',70,fam='Playfair Display',fill=K,style='font-style="italic"')
    s+=T(1510,430,'segelas teh, hati senang.',70,fam='Playfair Display',fill=Au,style='font-style="italic"')
    s+=f'<line x1="1330" y1="495" x2="1690" y2="495" stroke="{Au}" stroke-width="5"/>'+T(1510,570,'— TJAP DUA KOI',48,w=500,fill=K,ls=8)
    s+=lily(1300,815,80,True)+lily(1050,868,55)+lily(1860,860,60)
    s+=koi(1600,790,.55,rot=6,flip=True,pat=ORG)+koi(200,800,.5,rot=-6)
    return W,H,G,s
def papan(txt,fs,step):
    W,H=300,1000
    s=f'<path d="M60 0 L90 150 M240 0 L210 150" stroke="{Au}" stroke-width="10" stroke-dasharray="18 10" stroke-linecap="round"/>'
    s+=f'<rect x="40" y="140" width="220" height="840" rx="14" fill="{WOOD}"/><rect x="58" y="158" width="184" height="804" rx="8" fill="{G}" stroke="{Au}" stroke-width="8"/>'
    n=len(txt); y0=615-(n-1)*step/2
    for i,ch in enumerate(txt):
        if ch!=' ': s+=T(150,y0+i*step+fs*.35,ch,fs,fill=K if i<len(txt.split(' ')[0]) else Au)
    s+=stamp(115,180,70)
    return W,H,G,s
P={'2m-sisiA-emblem-200x90':sisiA,'2m-sisiB-rak-puisi-200x90':sisiB,'strip-2m-papan-kiri-30x100':lambda:papan('TOKO TEH',80,86),'strip-2m-papan-kanan-30x100':lambda:papan('DUA KOI',80,86)}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s)); open(f'p-{n}.html','w').write(wrapT(W,H,s))
def elev(low,sl,sr):
    EH=2300; g=f'<rect width="2000" height="{EH}" fill="{G}"/>'
    g+=f'<rect x="300" y="400" width="1400" height="1000" fill="#BCD9E3"/><text x="1000" y="920" text-anchor="middle" font-family="Inter" font-size="70" fill="#56655d">jendela ±140 cm</text>'
    g+=f'<g transform="translate(0 400)">{sl}</g><g transform="translate(1700 400)">{sr}</g><g transform="translate(0 1400)">{low}</g>'
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>body{{margin:0;background:#111}}svg{{display:block}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -80 2160 2460" width="700" height="797">{g}</svg></body></html>'
st=strip2()[3]
open('e-sisiA.html','w').write(elev(sisiA()[3],st,st))
open('e-sisiB.html','w').write(elev(sisiB()[3],P['strip-2m-papan-kiri-30x100']()[3],P['strip-2m-papan-kanan-30x100']()[3]))
