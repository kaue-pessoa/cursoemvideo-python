from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 e 5. Tente adivinhar!!')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO..')
sleep(3)
if jogador == computador:
    print('PARABENS! Voçê conseguiu me vencer!')
else:
    print('GANHEI!! Eu pensei no numero {} é não {}!'.format(computador, jogador))
