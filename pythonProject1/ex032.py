from datetime import date
from time import sleep
ano = int(input('Que ano quer analisar? Coloque 0 para analizar ano atual: '))
print('\n \033[1;33;40m...PROCESSANDO...\033[m \n')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} \033[1;36mÉ\033[m BISSEXTO'.format(ano))
else:
    print('O ano de {} \033[1;31mNÃO\033[m é BISSEXTO.'.format(ano))



#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#(from datetime import date) = importa a data do sistema
#date.today().year importa só o ano