exec(open('cup1.py').read().split("def art():")[0])
BW=740
def base(x0):
    g=f'<path d="M{x0+20} 585 Q{x0+BW/2} 610 {x0+BW-20} 585" fill="none" stroke="{INK}" stroke-width="5"/>'
    for t in (.15,.38,.62,.85): g+=f'<ellipse cx="{x0+BW*t}" cy="605" rx="12" ry="15" fill="{INK}"/>'
    for bx,bw,bh in ((20,130,80),(155,150,110),(310,140,135),(455,140,100),(600,120,80)):
        X=x0+bx;b_=730
        g+=f'<path d="M{X} {b_} V{b_-bh} L{X+bw/2} {b_-bh-28} L{X+bw} {b_-bh} V{b_} Z" fill="{INK}"/>'
        g+=f'<rect x="{X+bw*.18}" y="{b_-bh*.72}" width="{bw*.24}" height="{bh*.3}" rx="{bw*.1}" fill="{CLR}"/><rect x="{X+bw*.58}" y="{b_-bh*.72}" width="{bw*.24}" height="{bh*.3}" rx="{bw*.1}" fill="{CLR}"/>'
    return g+f'<rect x="{x0+20}" y="730" width="{BW-40}" height="30" rx="15" fill="{INK}"/>'
def art():
    X=[60,930,1800]; g=f'<rect width="2600" height="780" fill="{CLR}"/>'
    x=X[0]; c=x+BW/2
    g+=logomono(c-115,25,230)+T(c,395,'TOKO TEH',132,fill=INK,ls=4)+T(c,450,'TJAP DUA KOI',40,fam='Cinzel',fill=INK,ls=12)+T(c,500,'EST. 2025',26,fam='Inter',w=600,fill=INK,ls=6)
    x=X[1]; c=x+BW/2
    g+=f'<ellipse cx="{c}" cy="210" rx="230" ry="165" fill="none" stroke="{INK}" stroke-width="6"/>'+koim(c+20,145,.42,200)+koim(c-20,280,.42,20)
    g+=T(c,455,'Sepasang koi,',62,fam='Playfair Display',fill=INK,style='font-style="italic"')+T(c,530,'segelas teh.',62,fam='Playfair Display',fill=INK,style='font-style="italic"')
    x=X[2]; c=x+BW/2
    g+=mono(stamp(c-45,40,90),{R.upper()})
    g+=mono(igicon(c-200,195,64,K),{K.upper()})+T(c+50,247,'IG &amp; TikTok',40,fill=INK)
    g+=T(c,320,'@tokoteh.tjapduakoi',44,fam='Inter',w=700,fill=INK)
    g+=f'<line x1="{c-180}" y1="365" x2="{c+180}" y2="365" stroke="{INK}" stroke-width="4"/>'
    g+=T(c,425,'MAHAKAM LAMPION GARDEN',30,fam='Cinzel',fill=INK,ls=3)+T(c,470,'SAMARINDA',30,fam='Cinzel',fill=INK,ls=8)
    for x in X: g+=base(x)
    return g
A=art()
open('cup3.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>@page{{size:260mm 78mm;margin:0}}html,body{{margin:0}}svg{{display:block;width:260mm;height:78mm}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2600 780">{A}</svg></body></html>')
