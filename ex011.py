l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

m = l * a
t = m / 2

print('Sua parede tem a dimenção de {}x{} e sua área é de {}m².\nPara pintar essa parede, você precisará de {}l de tinta.'.format(l, a, m, t))