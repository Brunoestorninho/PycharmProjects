numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número digitado foi {} e ele é \033[34mPAR\033[m!'.format(numero))
else:
    print('O número digitado foi {} e ele é \033[31mÍMPAR\033[m!')
