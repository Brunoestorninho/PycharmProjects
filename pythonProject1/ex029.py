km = float(input('Qual a velocidade atual do carro? '))
multa = (km - 80) * 7.00
if km <= 80:
    print('Está no limite! \033[1;34mPARABÉNS\033[m!!!')
else:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    print('Você tera que pagar uma multa de \033[4;33mR${:.2f}\033[m!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

