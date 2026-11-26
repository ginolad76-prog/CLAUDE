exec(open("gen13.py").read().split("P={'2m-sisiA")[0])
W1,W2,W3='#8FAF8F','#6F9474','#5A846A'
def wav(W,y0):
    g=''
    for k_,c in ((0,W1),(70,W2),(140,W3)): g+=f'<path d="M0 {y0+k_} '+''.join('q100 -36 200 0 t200 0 ' for _ in range(W//400))+f'" fill="none" stroke="{c}" stroke-width="14" stroke-linecap="round"/>'
    return g
def kolamband():
    wy=0; wave=f'M0 {wy} '+''.join('q100 -50 200 0 t200 0 ' for _ in range(10))+f'V340 H0 Z'
    return f'<path d="{wave}" fill="{G}"/><path d="M0 80 '+''.join('q100 -40 200 0 t200 0 ' for _ in range(10))+f'" fill="none" stroke="{SAGE}" stroke-width="10"/>'
def riak(): return ''.join(f'<path d="M{-r} 0 A{r} {r*.55} 0 0 1 {r} 0" fill="none" stroke="{SAGE}" stroke-width="12"/>' for r in (500,620,740))
def tehtarik():
    return ''.join(T(0,i*70+(24 if i>=3 else 0),ch,70,fill=K if i<3 else Au) for i,ch in enumerate('TEHTARIK'))
def koiling():
    cx,cy,R=0,0,230; s=''
    for r,c in ((R+60,W2),(R+140,W3)): s+=f'<ellipse cx="{cx}" cy="{cy}" rx="{r*1.25}" ry="{r*.95}" fill="none" stroke="{c}" stroke-width="10"/>'
    s+=koi(cx+40,cy-150,.95,rot=200)+koi(cx-40,cy+150,.95,rot=20,pat=ORG)
    for x,y,r in ((cx-320,cy-170,14),(cx-350,cy-215,10),(cx+330,cy+150,14),(cx+360,cy+195,10)): s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{K}" stroke-width="6"/>'
    return s
E=[ # kode, jumlah, keterangan, svg
('D01-wordmark-toko-teh',1,'Sisi depan 4 m: TOKO TEH · TJAP DUA KOI',wordmark(0,0,300)),
('D02-kolam-ombak-400cm',1,'Sisi depan 4 m: pita kolam di bawah (boleh disambung per 2 m)',kolamband()),
('D03-riak-roda',1,'Sisi depan 4 m: 3 lengkung riak di atas roda',riak()),
('D04-koi-besar-merah',1,'Sisi depan 4 m: koi kiri',koi(0,0,1.0,rot=-4)),
('D05-koi-besar-oranye',1,'Sisi depan 4 m: koi kanan',koi(0,0,1.0,rot=4,flip=True,pat=ORG)),
('D06-lampion-besar',2,'Sisi depan 4 m: strip kiri & kanan jendela, atas',lantern(0,0,.8)),
('D07-huruf-teh-tarik-vertikal',1,'Sisi depan 4 m: strip kiri jendela',tehtarik()),
('D08-koi-kecil-naik-merah',1,'Sisi depan 4 m: strip kanan jendela',koi(0,0,.4,rot=-90,pat=R)),
('D09-koi-kecil-naik-oranye',1,'Sisi depan 4 m: strip kanan jendela',koi(0,0,.4,rot=-90,pat=ORG)),
('A01-emblem-est-2025',1,'Sisi 2 m A: tengah panel bawah',emblem(0,0,300)),
('A02-untaian-lampion-3',2,'Sisi 2 m A: kiri & kanan atas panel bawah',lstring(0,630,0,3,.42)),
('A03-lampion-sedang',2,'Sisi 2 m A: strip kiri & kanan jendela, atas',lantern(0,0,.62)),
('A04-koi-kecil-naik',4,'Sisi 2 m A: strip kiri & kanan (2 tiap strip)',koi(0,0,.32,rot=-90,pat=ORG)),
('B01-papan-gantung-toko-teh',1,'Sisi 2 m B: strip kiri jendela',papan('TOKO TEH',80,86)[3]),
('B02-papan-gantung-dua-koi',1,'Sisi 2 m B: strip kanan jendela',papan('DUA KOI',80,86)[3]),
('B03-koi-melingkar',1,'Sisi 2 m B: tengah panel bawah',koiling()),
('U01-ombak-garis-200cm',2,'Sisi 2 m A & B: dasar panel bawah',wav(2000,0)),
('U02-koi-sedang-merah',2,'Sisi 2 m A & B: kiri bawah',koi(0,0,.55,rot=-6)),
('U03-koi-sedang-oranye',2,'Sisi 2 m A & B: kanan bawah',koi(0,0,.5,rot=8,flip=True,pat=ORG)),
('U04-teratai-bunga',6,'Semua sisi: di garis air (2 depan, 2 tiap sisi 2 m)',lily(0,0,90,True)),
('U05-teratai-daun',6,'Semua sisi: di garis air',lily(0,0,65)),
('U06-stempel-sudut-cha',8,'Semua sisi: 2 sudut bawah tiap sisi',stamp(0,0,200)),
]
import json
json.dump([(c,q,k) for c,q,k,_ in E],open('el/list.json','w'))
for c,q,k,svg in E:
    open(f'el/{c}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="../fonts_local.css"><style>html,body{{margin:0;background:transparent}}</style></head><body><svg id="s" xmlns="http://www.w3.org/2000/svg" viewBox="-3000 -3000 6000 6000" width="600" height="600"><g id="g">{svg}</g></svg></body></html>')
