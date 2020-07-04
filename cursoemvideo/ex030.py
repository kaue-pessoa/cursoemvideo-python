distancia = float(input('Qual a distancia da sua viagem: '))
print('Voçê esta prestes a começar uma viagem de {}km.'.format(distancia))
#if distancia <= 200:
#    preço = distancia * 0.50
#else:
#    preço = distancia * 0.45
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagen e de R${:.2f}.'.format(preço))
