real = float(input('Quanto dinheiro voçê tem na carteira? R$ '))
dolar = real / 4.88
euro = real / 5.52
print('Com o valor R${:.2f} que voçê tem da para comprar US${:.2f} dolares ou este {:.2f} valor em Euro!'.format(real, dolar, euro))
