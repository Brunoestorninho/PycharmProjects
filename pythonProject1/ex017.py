#from math import hypot = importe somente o metodo da soma da hipotenusa
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(co, ca)
print('O comprimento da hipotenusa é: {:.2f}'.format(hip))

# math.hypot = soma do cateto da hipotenusa
