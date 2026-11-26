src=open('gen4.py').read(); exec(src[:src.index('def member')])
IG='tokoteh.tjapduakoi'
def qr2(x,y,size,url,dark=G):
    q=segno.make(url,error='m'); m=q.matrix; n=len(m); bd=2; cell=size/(n+2*bd)
    d=''.join(f'M{x+(c+bd)*cell:.2f} {y+(r+bd)*cell:.2f}h{cell+.3:.2f}v{cell+.3:.2f}h-{cell+.3:.2f}z' for r,row in enumerate(m) for c,v in enumerate(row) if v)
    return f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="8" fill="#fff"/><path d="{d}" fill="{dark}"/>'
def igicon(x,y,s,col):
    return f'<g fill="none" stroke="{col}" stroke-width="{s*.09}"><rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*.28}"/><circle cx="{x+s/2}" cy="{y+s/2}" r="{s*.22}"/></g><circle cx="{x+s*.76}" cy="{y+s*.24}" r="{s*.06}" fill="{col}"/>'
def uapLogo():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    cx=b+340; gw,gh=250,250; gx,gy=cx-gw/2,b+555
    s+=glass(gx,gy,gw,gh-20,False)
    for dx in (-.25,0,.25):
        sx=cx+gw*dx; s+=f'<path d="M{sx} {gy-20} c-28 -35 28 -55 0 -95" fill="none" stroke="{K}" stroke-opacity=".85" stroke-width="10" stroke-linecap="round"/>'
    s+=f'<path d="M{cx-150} {b+470} c-60 -60 -40 -170 10 -230 M{cx+150} {b+470} c60 -60 40 -170 -10 -230" fill="none" stroke="{K}" stroke-opacity=".45" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 16"/>'
    d=360; s+=L(cx-d/2,b+105,d)
    tx=b+955
    s+=T(tx,b+280,'IKUTI UAP',120,ls=4)+T(tx,b+405,'TEHNYA!',120,ls=4,fill=Au)
    pw,ph=640,96; px=tx-pw/2; py=b+445
    s+=f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="{ph/2}" fill="{K}"/>'+igicon(px+30,py+18,60,G)
    s+=T(px+pw/2+40,py+68,'@'+IG,56,fill=G,ls=1)
    qs=190; qx=px+20; qy=b+590
    s+=qr2(qx,qy,qs,'https://www.instagram.com/'+IG+'/')
    s+=T(qx+qs+30,qy+80,'Scan &amp; follow,',56,fam='Playfair Display',anc='start',style='font-style="italic"')
    s+=T(qx+qs+30,qy+150,'seduhan baru tiap hari.',39,w=500,anc='start',fill=Au,ls=2)
    return doc(W,H,s,u)
open('3-samping-uap-logo-140x90.html','w').write(uapLogo())
