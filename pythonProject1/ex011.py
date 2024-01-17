largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = (largura * altura) / 1.000
print('\nSua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
