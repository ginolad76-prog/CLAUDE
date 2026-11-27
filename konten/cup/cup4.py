exec(open('cup3.py').read().rsplit('def art():',1)[0])
def water(x0,y=600):
    g=''
    for k_,sw in ((0,7),(45,5),(90,4)):
        g+=f'<path d="M{x0+10} {y+k_} '+''.join('q46 -22 92 0 t92 0 ' for _ in range(4))+f'" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>'
    return g
def lilyo(x,y,r,flower=False):
    import math
    a=math.radians(14); ry=r*.45
    g=f'<path d="M{x} {y} L{x+r*math.cos(a):.1f} {y-ry*math.sin(a):.1f} A{r} {ry} 0 1 0 {x+r*math.cos(a):.1f} {y+ry*math.sin(a):.1f} Z" fill="none" stroke="{INK}" stroke-width="5"/>'
    if flower:
        for an in (-35,0,35): g+=f'<ellipse cx="{x}" cy="{y-r*.35}" rx="{r*.15}" ry="{r*.4}" fill="{INK}" transform="rotate({an} {x} {y-r*.05})"/>'
    return g
def rip(cx,cy,n=3,w=200):
    return ''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{w*(k+1)/n/2}" ry="{w*(k+1)/n/7}" fill="none" stroke="{INK}" stroke-width="5"/>' for k in range(n))
def bubbles(x,y): return ''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="{r}" fill="none" stroke="{INK}" stroke-width="4"/>' for dx,dy,r in ((0,0,10),(18,-30,7),(5,-55,5)))
def art():
    X=[60,930,1800]; g=f'<rect width="2600" height="780" fill="{CLR}"/>'
    # 1 sendirian + nama
    x=X[0]; c=x+BW/2
    g+=koim(c+10,190,.62,-6)+rip(c-260,250,2,120)+bubbles(c+250,110)
    g+=T(c,410,'TOKO TEH',120,fill=INK,ls=4)+T(c,462,'TJAP DUA KOI',38,fam='Cinzel',fill=INK,ls=12)
    g+=water(x)+lilyo(x+120,700,55,True)+lilyo(x+600,705,45)
    # 2 melompat
    x=X[1]; c=x+BW/2
    g+=koim(c,250,.55,-55)
    g+=f'<path d="M{c-180} 520 q60 -80 110 -10 M{c+70} 520 q50 -90 110 -5" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
    for dx,dy,r in ((-150,420,12),(-110,380,9),(130,430,11),(170,395,8),(-60,350,7)): g+=f'<circle cx="{c+dx}" cy="{dy}" r="{r}" fill="{INK}"/>'
    g+=f'<path d="M{c-230} 470 q100 -380 300 -400" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 12"/>'
    g+=mono(stamp(c+200,60,80),{R.upper()})
    g+=water(x,560)+lilyo(x+600,690,50,True)
    # 3 sepasang
    x=X[2]; c=x+BW/2
    g+=f'<ellipse cx="{c}" cy="215" rx="230" ry="160" fill="none" stroke="{INK}" stroke-width="5"/>'+koim(c+20,150,.42,200)+koim(c-20,280,.42,20)
    g+=T(c,440,'Sepasang koi,',58,fam='Playfair Display',fill=INK,style='font-style="italic"')+T(c,505,'segelas teh.',58,fam='Playfair Display',fill=INK,style='font-style="italic"')
    g+=T(c,560,'@tokoteh.tjapduakoi',30,fam='Inter',w=700,fill=INK)
    g+=water(x,620)+lilyo(x+130,720,45,True)
    return g
A=art()
open('cup4.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>@page{{size:260mm 78mm;margin:0}}html,body{{margin:0}}svg{{display:block;width:260mm;height:78mm}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2600 780">{A}</svg></body></html>')
