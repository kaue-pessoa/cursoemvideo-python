sal = float(input('Qual o valor do salario ? R$ '))
aumento = sal + (sal * 15 /100)
print('O salario do funcionario e de R${:.2f} e com o aumento de 15% vai para R${:.2f}.'.format(sal, aumento))
