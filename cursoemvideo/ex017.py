from math import radians, sin, cos,tan
ângulo = float(input('Digite o ângolo que voçê desaja:'))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(ângulo, tangente))
