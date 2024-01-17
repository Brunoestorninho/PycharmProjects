#import random
#n = random.randint(0,5)
#usuario = int(input('Qual numero de 0 a 5 o computador está pensando? '))
#if usuario == n:
#    print('PARABENS! Você acertou!')
#else:
#    print('QUE PENA! Você errou!')
#print('O numero pensado foi {}'.format(n))

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PESNSA" escolher aletoriamente
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
