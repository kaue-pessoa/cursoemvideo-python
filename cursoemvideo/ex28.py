velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!! Voçê esta acima do limite de velocidade!')
    multa =(velocidade - 80) * 7
    print('Voçê deve pagar uma multa de R$:{:.2f}'.format(multa))
print('Tenha um bom dia! Diriga com segurança!')
