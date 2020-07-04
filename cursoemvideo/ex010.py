l = float(input('Largura da parede? '))
a = float(input('Altura da parede? '))
d = l * a
print('Sua parede tem a dimensão de {}x{} é a sua area è {}m²'.format(l, a, d))
tinta = d / 2
print('Para pintar esta parede, voçê vai precisar de {}l de tinta.'.format(tinta))
