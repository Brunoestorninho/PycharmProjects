n = int(input('Digite um número: '))
d = n*2
t = n*3
r = float(n)**(1/2)
print('\nO número digitado é: {}.'.format(n))
print('O seu dobro é: {} \nSeu triplo é: {}.'.format(d, t))
print('A raiz quadrada de {} é: {:.0f}.'.format(n, r))
print('Raiz quadrada com outra função {} = {:.2f}.'.format(n, pow(n, (1/2))))
