exec(open("gen14.py").read().split("P={'2m-alt")[0])
SP='file:///home/user/CLAUDE/konten/stiker-penutup/'; LG='file:///home/user/CLAUDE/konten/logo-195cm/logo-toko-teh-diameter-195cm.svg'
EH=2300
def common(W,col):
    g=f'<rect y="-600" width="{W}" height="600" fill="none"/><rect width="{W}" height="{EH}" fill="{col}"/><rect width="{W}" height="100" fill="{G}"/><rect y="-40" width="{W}" height="40" fill="#E9ECEA"/>'
    return g
def finish(W):
    g=f'<rect x="0" y="1390" width="{W}" height="20" fill="{Au}"/>'
    g+=f'<g transform="translate(15 {EH-215})">{stamp(0,0,200)}</g><g transform="translate({W-215} {EH-215})">{stamp(0,0,200)}</g>'
    return g
def flap(x,w,img):  # penutup terbuka berdiri di atas jendela (hinge di atas jendela y=400)
    return f'<rect x="{x-10}" y="{400-900-10}" width="{w+20}" height="920" fill="#8E9592"/><image href="{img}" x="{x-20*w/ (w-40) if False else x}" y="{400-900}" width="{w}" height="900" preserveAspectRatio="none"/>'
def front():
    W=4000; _,_,_,low=kolam(); _,_,_,sl=strip4('L'); _,_,_,sr=strip4('R')
    g=common(W,M)+f'<rect x="400" y="400" width="3200" height="1000" fill="#BCD9E3"/>'
    g+=flap(400,3200,SP+'1-penutup-utama-320x90-preview.png')
    g+=f'<g transform="translate(0 400)">{sl}</g><g transform="translate(3600 400)">{sr}</g><g transform="translate(0 1400)">{low}</g>'+finish(W)
    g+=f'<circle cx="2000" cy="{EH+60}" r="330" fill="#1a1a1a"/><circle cx="2000" cy="{EH+60}" r="140" fill="#9a948a"/>'
    return W,g
def back():
    W=4000; g=common(W,M)+f'<rect x="3400" y="250" width="550" height="2050" fill="{G}" stroke="#0A3A26" stroke-width="12"/><rect x="3460" y="1250" width="20" height="160" fill="{Au}"/>'
    g+=f'<text x="3675" y="1000" text-anchor="middle" font-family="Inter" font-size="70" fill="#cfd8d2">pintu</text>'
    g+=finish(W)+f'<image href="{LG}" x="175" y="100" width="1950" height="1950"/>'
    g+=f'<circle cx="2000" cy="{EH+60}" r="330" fill="#1a1a1a"/><circle cx="2000" cy="{EH+60}" r="140" fill="#9a948a"/>'
    return W,g
def side(lowf,sl,sr,img):
    W=2000; _,_,_,low=lowf()
    g=common(W,G)+f'<rect x="300" y="400" width="1400" height="1000" fill="#BCD9E3"/>'+flap(300,1400,img)
    g+=f'<g transform="translate(0 400)">{sl}</g><g transform="translate(1700 400)">{sr}</g><g transform="translate(0 1400)">{low}</g>'+finish(W)
    return W,g
st=strip2()[3]; pk=papan('TOKO TEH',80,86)[3]; pn=papan('DUA KOI',80,86)[3]
V={'depan-4m-kolam':front(),'belakang-4m-logo':back(),
   '2m-A-emblem':side(sisiA,st,st,SP+'2-samping-komik-140x90-preview.png'),
   '2m-B-rak-puisi':side(sisiB,pk,pn,SP+'3-samping-uap-logo-140x90-preview.png'),
   '2m-alt-jam':side(jam,st,st,SP+'2-samping-komik-140x90-preview.png'),
   '2m-alt-mahakam':side(mahakam,st,st,SP+'3-samping-uap-logo-140x90-preview.png')}
def page(W,g,px):
    h=px*(EH+1300)/(W+200)
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts_local.css"><style>body{{margin:0;background:#dfe5e1}}svg{{display:block}}</style></head><body><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-100 -700 {W+200} {EH+1300}" width="{px}" height="{h:.0f}"><rect x="-100" y="{EH}" width="{W+200}" height="600" fill="#c9c4b8"/>{g}</svg></body></html>'
for n,(W,g) in V.items(): open(f'm-{n}.html','w').write(page(W,g,1400 if W==4000 else 800))
