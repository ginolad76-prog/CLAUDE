src=open('gen3.py').read(); exec(src[:src.index('def komik4')])
import segno
URL='https://tokotehtjapduakoi.github.io/kolam/'
def qr(x,y,size,dark=G):
    q=segno.make(URL,error='h',micro=False); m=q.matrix; n=len(m); bd=2; cell=size/(n+2*bd)
    g=f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="#FFFFFF"/>'
    d=''.join(f'M{x+(c+bd)*cell:.2f} {y+(r+bd)*cell:.2f}h{cell+.3:.2f}v{cell+.3:.2f}h-{cell+.3:.2f}z' for r,row in enumerate(m) for c,v in enumerate(row) if v)
    return g+f'<path d="{d}" fill="{dark}"/>'
def star(x,y,r): return f'<path d="M{x} {y-r} Q{x+r*.18} {y-r*.18} {x+r} {y} Q{x+r*.18} {y+r*.18} {x} {y+r} Q{x-r*.18} {y+r*.18} {x-r} {y} Q{x-r*.18} {y-r*.18} {x} {y-r}Z" fill="{Au}"/>'
def member():
    W,H,u=1400,900,30; b=B; s=frame(W,H,b,24,u)
    s+=T(b+700,b+180,'GABUNG MEMBER KOLAM KOI',92,ls=4,fill=Au)
    k=.76; pw=PW*k; Y=b+225; x0=b+90; gap=20
    P=[]
    # 1 beli
    body=glass(50,170,170,240,True)
    body+=f'<path d="M225 150 h115 v230 l-14 12 -14 -12 -15 12 -14 -12 -15 12 -14 -12 -15 12 -14 -12 z" fill="{K}"/>'
    for j in range(4): body+=f'<rect x="245" y="{185+j*28}" width="{75 if j%2 else 55}" height="9" fill="#B9B19F"/>'
    body+=f'<rect x="250" y="305" width="40" height="40" fill="none" stroke="{G}" stroke-width="7"/><rect x="262" y="317" width="16" height="16" fill="{G}"/>'
    P.append(('Beli teh',body))
    # 2 scan & daftar
    body=f'<rect x="95" y="70" width="170" height="340" rx="28" fill="#0C3322" stroke="{K}" stroke-width="10"/><rect x="110" y="105" width="140" height="265" rx="8" fill="#16573C"/>'
    body+=koi(180,190,.2,rot=-15)+f'<rect x="125" y="300" width="110" height="42" rx="21" fill="{Au}"/>'+T(180,331,'DAFTAR',28,fill=G)
    body+=f'<rect x="160" y="82" width="40" height="8" rx="4" fill="{K}"/>'
    P.append(('Scan &amp; daftar',body))
    # 3 tarik kartu
    body=''
    for rot,pat in ((-16,ORG),(0,R),(16,ORG)):
        body+=f'<g transform="rotate({rot} 180 420)"><rect x="115" y="150" width="130" height="190" rx="12" fill="{K}" stroke="{Au}" stroke-width="7"/><rect x="127" y="162" width="106" height="166" rx="7" fill="none" stroke="{Au}" stroke-width="3"/></g>'
    body+=koi(180,245,.24,rot=-70,pat=R)
    body+=star(80,110,26)+star(290,90,20)+star(300,200,14)+star(60,250,14)
    P.append(('Tarik kartu!',body))
    for i,(cap,body) in enumerate(P):
        x=x0+i*(pw+gap)
        s+=f'<g transform="translate({x} {Y}) scale({k})">'+panel(0,0,PW,PH,cap,body,64)+num(30,30,str(i+1))+'</g>'
    # QR block
    qx=x0+3*(pw+gap)+18; qw=b+1305-qx; qy=Y
    s+=f'<rect x="{qx}" y="{qy}" width="{qw}" height="{PH*k}" rx="18" fill="{K}"/>'
    qs=min(qw-40,PH*k-110); s+=qr(qx+(qw-qs)/2,qy+22,qs)
    s+=T(qx+qw/2,qy+qs+85,'SCAN DI SINI',54,fill=G,ls=3)
    s+=T(qx+qw/2,qy+PH*k+67,'Gratis daftarnya!',44,fam='Playfair Display',fill=K,style='font-style="italic"')
    return doc(W,H,s,u)
def logoS():
    W,H,u=1400,900,40; b=B; s=frame(W,H,b,30,u)
    d=700; s+=L(b+W/2-d/2,b+H/2-d/2,d)
    s+=cloud(b+150,b+H-170,1.0)+cloud(b+1250,b+H-170,1.0,True)+cloud(b+160,b+260,.8)+cloud(b+1240,b+260,.8,True)
    return doc(W,H,s,u)
for n,f in (('2-samping-member-140x90',member),('3-samping-logo-140x90',logoS)): open(n+'.html','w').write(f())
