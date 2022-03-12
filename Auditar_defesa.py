# Programa para verificar determinados tópicos em uma peça

arquivo = str(input('Cole aqui o texto da peça: '))

# Tópicos que serão verificados
preliminar = ['Tópico 1',
              'Tópico 2', 'Tópico 3']

merito = ['Tópico 1',
          'Tópico 2',
          'Tópico 3',
          'Tópico 4',
          'Tópico 5',
          'Tópico 6']

# Verificação dos tópicos no texto inserido

for texto in arquivo:
    found = False
    for palavra in texto.split():
        if palavra in preliminar:
            print(f'Tópico encontrado: {palavra}')
            found = True
            break

else:
    print('Preliminar não encontrada.')

for texto in arquivo:
    found = False
    for palavra1 in texto.split():
        if palavra1 in merito:
            print(f'Tópico encontrado: {palavra1}')
            found = True
            break

else:
    print('Mérito não encontrado.')
