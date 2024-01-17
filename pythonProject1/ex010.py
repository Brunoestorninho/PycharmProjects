real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/4.97 #dolar em 05/09/23
euro = real/5.33 #euro em 05/09/23
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${} você pode comprar EUR${:.2f}'.format(real, euro))
