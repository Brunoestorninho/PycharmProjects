n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2 #soma
m = n1*n2 #multiplicação
d = n1/n2 #divisão
di = n1//n2 #divisão inteira
e = n1**n2 #expotenciação
print('A soma é {}, a multiplicação é {}, a divisão é {:.2f}'.format(s, m, d)) #{:.2f}casas decimais flutuantes
print('divisão inteira {}, e potência {:.3f}'.format(di, e))
