src=open('gen2.py').read(); exec(src[:src.index('# ===== UTAMA')])
PW,PH=360,520
def komik4():
    W,H,u=1400,900,30; b=B; s=frame(W,H,b,24,u); k=.82; pw=PW*k; gap=(1230-4*pw)/3; Y=b+200
    P=[]
    # 1
    body=ripples(180,400,300)+ripples(90,150,120,2)+koi(175,330,.42,rot=-8)
    body+=f'<circle cx="300" cy="250" r="10" fill="none" stroke="{K}" stroke-width="4"/><circle cx="318" cy="210" r="7" fill="none" stroke="{K}" stroke-width="4"/>'
    P.append(('Sendirian…',body))
    # 2
    body=f'<rect x="0" y="0" width="{PW}" height="{PH*.42}" fill="#16573C"/>'+glass(120,40,120,150)+ripples(180,PH*.42+20,320,2)+koi(165,390,.42,rot=-35)+T(290,330,'!',120,fill=Au)
    for j in range(3): body+=f'<path d="M{150+j*30} 200 q-20 40 0 80 q20 40 0 80" fill="none" stroke="{K}" stroke-opacity=".7" stroke-width="5" stroke-dasharray="10 12"/>'
    P.append(('Wangi apa ini?',body))
    # 3
    body=f'<rect x="0" y="{PH*.68}" width="{PW}" height="{PH}" fill="#0C3322"/><path d="M0 {PH*.68} q45 -18 90 0 t90 0 t90 0 t90 0" fill="none" stroke="{K}" stroke-width="5"/>'+koi(190,220,.42,rot=-50)
    body+=f'<path d="M80 {PH*.68} q20 -60 40 -10 M230 {PH*.68} q25 -70 45 -5" fill="none" stroke="{K}" stroke-width="7" stroke-linecap="round"/>'
    for cx,cy,r in ((90,300,10),(120,260,8),(260,300,9),(290,270,7)): body+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{K}"/>'
    P.append(('Hup!',body))
    # 4
    inner=koi(150,290,.25,rot=-20)+koi(215,390,.25,rot=160,pat=ORG)
    body=glass(60,120,240,360,False,inner)+f'<path d="M180 60 c-30 -30 -60 0 -30 25 l30 25 l30 -25 c30 -25 0 -55 -30 -25 z" fill="{R}"/>'
    P.append(('Ketemu deh!',body))
    for i,(cap,body) in enumerate(P):
        x=b+85+i*(pw+gap)
        s+=f'<g transform="translate({x} {Y}) scale({k})">'+panel(0,0,PW,PH,cap,body,60)+num(30,30,str(i+1))+'</g>'
    return doc(W,H,s,u)
def uapKoi():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    gx,gw,gh,gy=b+200,260,280,b+490
    s+=glass(gx,gy,gw,gh,False)
    cx,cy=gx+gw/2,b+255
    for j,dx in enumerate((-.25,0,.25)):
        sx=cx+gw*dx; s+=f'<path d="M{sx} {gy-25} c-30 -45 30 -70 0 -120" fill="none" stroke="{K}" stroke-opacity=".85" stroke-width="10" stroke-linecap="round"/>'
    s+=f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="{K}" stroke-opacity=".35" stroke-width="5" stroke-dasharray="6 16" stroke-linecap="round"/>'
    s+=koi(cx+15,cy-70,.36,rot=195)+koi(cx-15,cy+70,.36,rot=15,pat=ORG)
    tx=b+935
    s+=T(tx,b+360,'TARIK NAPAS,',118,ls=4)
    s+=T(tx,b+520,'TARIK TEH.',118,ls=4,fill=Au)
    s+=f'<line x1="{tx-260}" y1="{b+590}" x2="{tx+260}" y2="{b+590}" stroke="{Au}" stroke-width="4"/>'
    s+=T(tx,b+680,'Sepasang koi, segelas teh',58,fam='Playfair Display',style='font-style="italic"')
    return doc(W,H,s,u)
for n,f in (('2-samping-komik-140x90',komik4),('3-samping-uap-koi-140x90',uapKoi)): open(n+'.html','w').write(f())
