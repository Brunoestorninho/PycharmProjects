print('-=' * 15, '\nAnalizador de triângulo')
print('-=' * 15)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('\033[1;33mOs segmento acima PODEM FORMAR um triângulo.\033[m')
else:
    print('\033[4;31mOs segmento acima NÃO PODEM FORMAR um triângulo.\033[m')


#Desenvolva um programa que leia o comprimento de três retas e
#diga ao usuário se elas podem ou não formar um triângulo.