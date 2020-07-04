dia = int(input('Quantos dia com o carro? '))
km = float(input('Quandos quilomentos foram rodados? '))
v = (dia*60) + (km*0.15)
print('O total a ser pago e de {:.2f}'.format(v))
