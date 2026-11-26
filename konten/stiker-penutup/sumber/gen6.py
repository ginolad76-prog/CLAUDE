src=open('gen5.py').read(); exec(src[:src.index('def uapLogo')])
GREY='#8E9A94'
def komikB():
    W,H,u=1400,900,30; b=B; s=frame(W,H,b,24,u); k=.82; pw=PW*k; gap=(1230-4*pw)/3; Y=b+200
    P=[]
    # 1 berat
    body=''.join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{GREY}"/>' for cx,cy,rx,ry in ((140,110,70,45),(210,95,75,55),(265,120,55,38),(180,135,95,35)))
    body+=''.join(f'<line x1="{x}" y1="{y}" x2="{x-10}" y2="{y+35}" stroke="{GREY}" stroke-width="6" stroke-linecap="round"/>' for x,y in ((120,185),(170,205),(220,180),(260,210),(150,250),(240,250)))
    body+=ripples(180,440,300,2)+koi(180,370,.4,rot=18)
    P.append(('Hari ini berat…',body))
    # 2 mampir
    body=f'<rect x="0" y="420" width="{PW}" height="120" fill="#0C3322"/>'
    body+=f'<rect x="150" y="230" width="190" height="170" rx="10" fill="{M}"/><rect x="150" y="230" width="190" height="16" fill="{G}"/><rect x="172" y="268" width="146" height="70" fill="{K}"/>'
    body+=f'<path d="M168 262 L322 262 L345 205 L190 205 Z" fill="{G}" stroke="{Au}" stroke-width="5"/>'
    body+=f'<circle cx="190" cy="410" r="20" fill="#111"/><circle cx="300" cy="410" r="20" fill="#111"/>'
    body+=lantern(110,40,.45)
    body+=koi(80,345,.26,rot=0)+f'<path d="M20 330 h-0" />'+''.join(f'<circle cx="{x}" cy="345" r="5" fill="{K}" fill-opacity=".6"/>' for x in (20,40))
    P.append(('Mampir dulu.',body))
    # 3 ditarik
    body=f'<g transform="rotate(-40 95 120)"><rect x="55" y="80" width="80" height="85" rx="8" fill="#C9CDCC" stroke="{K}" stroke-width="6"/><path d="M135 100 q30 0 30 25 q0 25 -30 25" fill="none" stroke="#C9CDCC" stroke-width="10"/></g>'
    body+=f'<path d="M140 150 C200 210 252 250 250 318 L222 318 C222 260 175 220 126 165 Z" fill="{TEA}"/>'
    body+=glass(170,315,140,170,False)
    body+=star(290,120,22)+star(70,300,16)+star(320,250,13)
    P.append(('Tehnya ditarik…',body))
    # 4 enaknya
    body=f'<circle cx="290" cy="85" r="42" fill="{Au}"/>'+''.join(f'<line x1="{290+60*c}" y1="{85+60*s_}" x2="{290+82*c}" y2="{85+82*s_}" stroke="{Au}" stroke-width="7" stroke-linecap="round"/>' for c,s_ in ((1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)))
    body+=glass(195,250,120,170,False)+f'<path d="M260 230 L240 330" stroke="{M}" stroke-width="9" stroke-linecap="round"/>'
    body+=koi(130,340,.32,rot=-15)
    body+=f'<path d="M90 190 c-14 -14 -28 0 -14 12 l14 12 l14 -12 c14 -12 0 -26 -14 -12 z" fill="{R}"/><path d="M60 250 c-10 -10 -20 0 -10 9 l10 9 l10 -9 c10 -9 0 -19 -10 -9 z" fill="{R}"/>'
    P.append(('Ahh… enaknya!',body))
    for i,(cap,body) in enumerate(P):
        x=b+85+i*(pw+gap)
        s+=f'<g transform="translate({x} {Y}) scale({k})">'+panel(0,0,PW,PH,cap,body,50)+num(30,30,str(i+1))+'</g>'
    return doc(W,H,s,u)
open('2-samping-komik-140x90.html','w').write(komikB())
