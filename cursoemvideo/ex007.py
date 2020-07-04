m = float(input('Uma distâcia em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A media de {}m corresponde a {},km{}hm,{}dam,{:.0f}dm ,{:.0f}cm e tantos {:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))
