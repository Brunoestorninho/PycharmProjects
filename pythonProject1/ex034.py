salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganhava R$\033[4;31m{:.2f}\033[m passa a ganhar R$\033[4;33m{:.2f}\033[m agora'.format(salario, aumento))








#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.