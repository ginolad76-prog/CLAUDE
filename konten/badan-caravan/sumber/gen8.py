CUPDEF='''
TAN='#D9B78E'
def cup(x,y,w,h,detail=True):
    i=uid(); bw=w*.8; o=(w-bw)/2; cx=x+w/2
    p=f'M{x} {y} L{x+w} {y} L{x+w-o} {y+h} L{x+o} {y+h} Z'
    g=f'<clipPath id="{i}"><path d="{p}"/></clipPath><defs><linearGradient id="t{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EFDDC0"/><stop offset=".45" stop-color="#D3AA7A"/><stop offset="1" stop-color="#B98957"/></linearGradient></defs>'
    g+=f'<g clip-path="url(#{i})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#t{i})"/>'
    # logo kecil
    if detail: g+=L(cx-w*.13,y+h*.06,w*.26).replace(f'fill="{K}"/><circle','fill="none"/><circle',1)
    # papan TOKO TEH
    sw,sh=w*.72,h*.17; sy=y+h*(.3 if detail else .2)
    g+=f'<rect x="{cx-sw/2}" y="{sy}" width="{sw}" height="{sh}" rx="{w*.02}" fill="{G}"/><rect x="{cx-sw/2+w*.025}" y="{sy+w*.025}" width="{sw-w*.05}" height="{sh-w*.05}" fill="none" stroke="{TAN}" stroke-width="{w*.01}"/>'
    g+=T(cx,sy+sh*.71,'TOKO TEH',w*.115,fill=TAN,ls=w*.012)
    ry=sy+sh+h*.03; rw=w*.56
    g+=f'<path d="M{cx-rw/2} {ry} H{cx+rw/2} l-{w*.03} {h*.03} l{w*.03} {h*.03} H{cx-rw/2} l{w*.03} -{h*.03} z" fill="{G}"/>'
    if detail: g+=T(cx,ry+h*.045,'TJAP DUA KOI',w*.045,fam='Cinzel',fill=TAN,ls=w*.012)
    # untaian lampion + deretan ruko
    ly=y+h*.64; g+=f'<path d="M{x} {ly} Q{cx} {ly+h*.03} {x+w} {ly}" fill="none" stroke="{G}" stroke-width="{w*.008}"/>'
    for t in (.15,.38,.62,.85): g+=f'<ellipse cx="{x+w*t}" cy="{ly+h*.035}" rx="{w*.022}" ry="{h*.022}" fill="{G}"/>'
    by=y+h*.83
    for bx,bwid,bh in ((.02,.2,.1),(.22,.18,.13),(.42,.22,.16),(.66,.16,.12),(.84,.2,.1)):
        X=x+w*bx; Wd=w*bwid; Hh=h*bh
        g+=f'<path d="M{X} {by} V{by-Hh} L{X+Wd/2} {by-Hh-h*.035} L{X+Wd} {by-Hh} V{by} Z" fill="{G}"/>'
        g+=f'<rect x="{X+Wd*.2}" y="{by-Hh*.75}" width="{Wd*.25}" height="{Hh*.35}" rx="{Wd*.1}" fill="url(#t{i})"/><rect x="{X+Wd*.55}" y="{by-Hh*.75}" width="{Wd*.25}" height="{Hh*.35}" rx="{Wd*.1}" fill="url(#t{i})"/>'
    g+=f'<rect x="{x}" y="{by}" width="{w}" height="{h*.14}" fill="{G}"/>'
    if detail: g+=T(cx,by+h*.085,'@tokoteh.tjapduakoi',w*.045,fam='Inter',w=600,fill=TAN)
    g+=f'<rect x="{x+w*.12}" y="{y}" width="{w*.05}" height="{h}" fill="#fff" fill-opacity=".22"/><rect x="{x+w*.8}" y="{y}" width="{w*.025}" height="{h}" fill="#fff" fill-opacity=".15"/></g>'
    g+=f'<path d="{p}" fill="none" stroke="{K}" stroke-width="{w*.022}" stroke-linejoin="round"/>'
    g+=f'<ellipse cx="{cx}" cy="{y}" rx="{w/2+w*.02}" ry="{w*.035}" fill="#E4E9E8" stroke="{K}" stroke-width="{w*.015}"/>'
    return g
'''
g6=open('gen6.py').read().replace("open('2-samping-komik-140x90.html','w').write(komikB())","")
g6=g6.replace("def komikB():",CUPDEF+"\ndef komikB():",1)
g6=g6.replace("glass(170,315,140,170,False)","cup(165,305,150,195,False)")
g6=g6.replace("glass(195,250,120,170,False)+f'<path d=\"M260 230 L240 330\" stroke=\"{M}\" stroke-width=\"9\" stroke-linecap=\"round\"/>'",
              "f'<path d=\"M270 215 L250 300\" stroke=\"{M}\" stroke-width=\"9\" stroke-linecap=\"round\"/>'+cup(190,240,135,200,False)")
exec(g6)
g5=open('gen5.py').read().replace("open('3-samping-uap-logo-140x90.html','w').write(uapLogo())","")
g5=g5.replace("s+=glass(gx,gy,gw,gh-20,False)","s+=cup(gx,gy-20,gw,gh+10,True)")
exec(g5)
g7=open('gen7.py').read(); g7=g7[g7.index('def garland'):]
g7=g7.replace("src5=open('gen5.py').read()\nfor a,c in ((\"'IKUTI UAP',120\",\"'IKUTI UAP',120\"),):pass\n","")
exec(g7)
