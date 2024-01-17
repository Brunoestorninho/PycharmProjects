frase = 'Curso em Vídeo Python' #cadeia de caractere é uma string
print(frase[9:15]) #fatia o texto
print(len(frase)) #lê o número de caracteres
print(frase.count('o')) #conta quantas vezes a letra aparece
print(frase.find('deo')) #mostra aonde começa
print(frase.find('Android')) #quando não acha na frase aparece -1
print('Curso'in frase) #retorna verdadeiro ou falso uma palavra se consta na frase
print(frase.replace('Python','Android')) #troca uma palavra
print(frase.upper()) #muda toda a frase para maiusculo
print(frase.lower()) #muda toda a frase para minusculo
print(frase.capitalize()) #deixa só o primeiro caracter da string em maiusculo
print(frase.title()) #divide palavra por palavra e todas ficam rm maiusculas
#print(frase.strip()) #tira os espaços vazis do começo e final da frase (.rstrip()) lado direito - (.lstrip()) lado esquerdo
