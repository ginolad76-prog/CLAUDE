import re
exec(open("gen5.py").read().split("def uapLogo")[0])
INK='#000000'; CLR='#FFFFFF'
def mono(svg,ink):
    def f(m):
        c=m.group(2).upper(); return f'{m.group(1)}="{INK if c in ink else CLR}"'
    return re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"',f,svg)
def logomono(x,y,d):
    l=open('logo.svg').read(); l=re.sub(r'<\?xml.*?\?>|<!--.*?-->','',l,flags=re.S)
    def f(m):
        h=m.group(1); r,g,b=int(h[1:3],16),int(h[3:5],16),int(h[5:7],16)
        return f'fill="{INK if (r>150 and b<110) else CLR}"'
    l=re.sub(r'fill="(#[0-9A-Fa-f]{6})"',f,l)
    return re.sub(r'width="3200" height="3200"',f'x="{x}" y="{y}" width="{d}" height="{d}"',l,count=1)
PW,PH=650,780
def skyline(x0):
    g=f'<path d="M{x0} 575 Q{x0+325} 600 {x0+650} 575" fill="none" stroke="{INK}" stroke-width="5"/>'
    for t in (.12,.37,.63,.88): g+=f'<ellipse cx="{x0+650*t}" cy="{595}" rx="13" ry="16" fill="{INK}"/>'
    for bx,bw,bh in ((0,120,90),(125,140,120),(270,150,140),(425,120,105),(550,100,90)):
        X=x0+bx;base=735
        g+=f'<path d="M{X} {base} V{base-bh} L{X+bw/2} {base-bh-30} L{X+bw} {base-bh} V{base} Z" fill="{INK}"/>'
        g+=f'<rect x="{X+bw*.18}" y="{base-bh*.72}" width="{bw*.24}" height="{bh*.3}" rx="{bw*.1}" fill="{CLR}"/><rect x="{X+bw*.58}" y="{base-bh*.72}" width="{bw*.24}" height="{bh*.3}" rx="{bw*.1}" fill="{CLR}"/>'
    return g+f'<rect x="{x0}" y="735" width="650" height="45" fill="{INK}"/>'
def koim(x,y,s,rot,flip=False):
    return mono(koi(x,y,s,rot=rot,flip=flip),{Au.upper(),R.upper(),ORG.upper(),G.upper()})
def art():
    g=f'<rect width="{PW*4}" height="{PH}" fill="{CLR}"/>'
    # 1 depan
    x=0; g+=logomono(x+205,30,240)
    g+=T(x+325,410,'TOKO TEH',128,fill=INK,ls=4)+T(x+325,462,'TJAP DUA KOI',40,fam='Cinzel',fill=INK,ls=12)+T(x+325,515,'EST. 2025',26,fam='Inter',w=600,fill=INK,ls=6)
    # 2 sepasang koi
    x=650; g+=f'<ellipse cx="{x+325}" cy="270" rx="250" ry="200" fill="none" stroke="{INK}" stroke-width="6"/>'
    g+=koim(x+345,190,.5,200)+koim(x+305,350,.5,20)
    # 3 slogan
    x=1300; g+=T(x+325,230,'Sepasang koi,',72,fam='Playfair Display',fill=INK,style='font-style="italic"')+T(x+325,320,'segelas teh.',72,fam='Playfair Display',fill=INK,style='font-style="italic"')
    g+=mono(stamp(x+290,380,70),{R.upper()})+koim(x+170,110,.22,-10)+koim(x+480,470,.22,170)
    # 4 info permanen
    x=1950; g+=mono(igicon(x+160,170,70,K),{K.upper()})+T(x+360,228,'IG &amp; TikTok',38,fill=INK)
    g+=T(x+325,300,'@tokoteh.tjapduakoi',44,fam='Inter',w=700,fill=INK)
    g+=f'<line x1="{x+150}" y1="345" x2="{x+500}" y2="345" stroke="{INK}" stroke-width="4"/>'
    g+=T(x+325,410,'MAHAKAM LAMPION GARDEN',30,fam='Cinzel',fill=INK,ls=3)+T(x+325,455,'SAMARINDA',30,fam='Cinzel',fill=INK,ls=8)
    for i in range(4): g+=skyline(i*650)
    return g
A=art()
open('cup1.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>@page{{size:260mm 78mm;margin:0}}html,body{{margin:0}}svg{{display:block;width:260mm;height:78mm}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2600 780">{A}</svg></body></html>')
