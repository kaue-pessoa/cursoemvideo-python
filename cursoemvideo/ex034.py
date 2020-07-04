print('-=-' * 25)
print('Analizador de triângulos')
print('-=-' * 25)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimento acima NÂO PODEM FORMAR triângulo!')
