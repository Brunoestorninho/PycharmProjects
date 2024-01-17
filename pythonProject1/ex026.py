frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()
print('A letra "A" aparece',frase.count('a'), 'vezes.')
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))

