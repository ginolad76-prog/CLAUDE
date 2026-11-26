exec(open('gen6.py').read().replace("open('2-samping-komik-140x90.html','w').write(komikB())",""))
exec(open('gen5.py').read().replace("open('3-samping-uap-logo-140x90.html','w').write(uapLogo())",""))
def garland(x1,x2,y,sag,n,s):
    g=f'<path d="M{x1} {y} Q{(x1+x2)/2} {y+2*sag} {x2} {y}" fill="none" stroke="{Au}" stroke-width="4"/>'
    for i in range(n):
        t=(i+.5)/n; px=x1+(x2-x1)*t; py=y+2*sag*2*t*(1-t)
        g+=lantern(px,py,s)
    for i in range(n+1):
        t=i/n; px=x1+(x2-x1)*t; py=y+2*sag*2*t*(1-t); g+=f'<circle cx="{px}" cy="{py}" r="7" fill="{K}"/><circle cx="{px}" cy="{py}" r="14" fill="{K}" fill-opacity=".25"/>'
    return g
def add(html,orn): return html.replace('</svg></body>',orn+'</svg></body>')
b=B
k=komikB()
k=add(k,garland(b+95,b+1305,b+78,22,8,.22)+cloud(b+100,b+800,.75)+cloud(b+1300,b+800,.75,True)
   +T(b+700,b+790,'Sepasang koi, segelas teh',46,fam='Playfair Display',fill=Au,style='font-style="italic"'))
open('2-samping-komik-140x90.html','w').write(k)
src5=open('gen5.py').read()
for a,c in (("'IKUTI UAP',120","'IKUTI UAP',120"),):pass
u=uapLogo()
u=add(u,garland(b+660,b+1250,b+96,8,5,.17)+cloud(b+92,b+800,.5)+cloud(b+590,b+800,.5,True)
   +star(b+125,b+170,20)+star(b+560,b+150,16)+star(b+110,b+470,13)+star(b+575,b+420,18))
open('3-samping-uap-logo-140x90.html','w').write(u)
