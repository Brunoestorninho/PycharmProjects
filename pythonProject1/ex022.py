nome = str(input('Digite o nome completo: ')).strip() #.strip elimina espaços antes e depois cado nescessário
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # -count para eliminar um espaço vazio (' ')
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #contando até o primeiro espaço
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))