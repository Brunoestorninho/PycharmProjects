km = float(input('Qual a distacia da sua viagem? '))
distancia = km * 0.50
longa = km * 0.45
print('Você está prestes a começar uma viagem de {}km.'.format(km))
if km <= 200:
    print('O preço da passagem será de R${:.2f}.'.format(distancia))
else:
    print('O preço da passagem será de R${:.2f}.'.format(longa))





#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.