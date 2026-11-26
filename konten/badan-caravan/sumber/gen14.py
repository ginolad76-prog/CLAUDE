import math
exec(open("gen13.py").read().split("P={'2m-sisiA")[0])
def jam():
    W,H=2000,900; s=waves2(W,740); cx,cy,r=700,380,300
    s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{Au}"/><circle cx="{cx}" cy="{cy}" r="{r*.92}" fill="{M}"/><circle cx="{cx}" cy="{cy}" r="{r*.84}" fill="{K}"/>'
    for i in range(60):
        a=math.radians(i*6); l=.1 if i%5==0 else .04
        s+=f'<line x1="{cx+r*.8*math.sin(a):.1f}" y1="{cy-r*.8*math.cos(a):.1f}" x2="{cx+r*(.8-l)*math.sin(a):.1f}" y2="{cy-r*(.8-l)*math.cos(a):.1f}" stroke="{G}" stroke-width="{8 if i%5==0 else 4}"/>'
    for n,a in (('12',0),('3',90),('6',180),('9',270)):
        A=math.radians(a); s+=T(cx+r*.58*math.sin(A),cy-r*.58*math.cos(A)+r*.08,n,r*.2,fill=G)
    s+=T(cx,cy-r*.25,'JAM TEH',r*.09,fam='Cinzel',fill=M,ls=6)+stamp(cx-r*.09,cy+r*.24,r*.18)
    for ang,ln,wd in ((120,.42,14),(20,.62,9)):
        A=math.radians(ang); s+=f'<line x1="{cx}" y1="{cy}" x2="{cx+r*ln*math.sin(A):.1f}" y2="{cy-r*ln*math.cos(A):.1f}" stroke="{G}" stroke-width="{wd}" stroke-linecap="round"/>'
    s+=f'<circle cx="{cx}" cy="{cy}" r="14" fill="{Au}"/>'
    s+=T(1420,360,'Selalu',110,fam='Playfair Display',fill=K,style='font-style="italic"')+T(1420,500,'waktunya teh.',110,fam='Playfair Display',fill=Au,style='font-style="italic"')
    s+=koi(250,800,.5,rot=-6)+koi(1770,790,.5,rot=8,flip=True,pat=ORG)+lily(1450,860,60,True)
    return W,H,G,s
def mahakam():
    W,H=2000,900; s=f'<path d="M1690 120 a90 90 0 1 0 70 150 a70 70 0 1 1 -70 -150 Z" fill="{Au}"/>'
    for x,y in ((1450,120),(1550,230),(160,120),(1000,90),(1250,170)): s+=star(x,y,18)
    dy=560; s+=f'<rect x="80" y="{dy}" width="1840" height="22" fill="{K}"/>'
    for a,b_ in ((180,760),(760,1240),(1240,1820)):
        m=(a+b_)/2; h=220 if b_-a>500 else 160
        s+=f'<path d="M{a} {dy} Q{m} {dy-2*h} {b_} {dy}" fill="none" stroke="{K}" stroke-width="14"/>'
        for i in range(1,8):
            x=a+(b_-a)*i/8; t=i/8; y=dy-2*h*2*t*(1-t)*1
            s+=f'<line x1="{x}" y1="{dy}" x2="{x}" y2="{y:.0f}" stroke="{K}" stroke-width="7"/>'
    for x in (180,760,1240,1820): s+=f'<rect x="{x-18}" y="{dy}" width="36" height="150" fill="{K}"/>'
    s+=waves2(W,700)
    s+=f'<path d="M560 690 h170 l-30 40 h-110 z" fill="{WOOD}"/><line x1="640" y1="690" x2="640" y2="610" stroke="{K}" stroke-width="6"/><path d="M645 615 l60 60 h-60 z" fill="{K}"/>'
    s+=koi(1150,800,.5,rot=-4,pat=ORG)+koi(300,810,.42,rot=4)+lily(1650,850,70,True)
    s+=T(560,230,'dari tepi Mahakam',90,fam='Playfair Display',fill=Au,style='font-style="italic"')
    return W,H,G,s
def sudut():
    W,H=200,200; return W,H,M,stamp(10,10,180)
P={'2m-alt-jam-kopitiam-200x90':jam,'2m-alt-mahakam-malam-200x90':mahakam,'stempel-sudut-20x20':sudut}
for n,f in P.items():
    W,H,bg,s=f(); open(f'b-{n}.html','w').write(wrap(W,H,bg,s)); open(f'p-{n}.html','w').write(wrapT(W,H,s))
