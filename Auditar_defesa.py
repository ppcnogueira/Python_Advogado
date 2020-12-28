# Programa para verificar determinados tópicos em uma peça

arquivo = str(input('Cole aqui o texto da peça: '))

# Tópicos que serão verificados
preliminar = ['DA INCONSTITUCIONALIDADE DA LEI 8842/2020 - ADI 6495',
              'DA INCONSTITUCIONALIDADE DA LEI LOCAL 2.472/2020', 'DA ILEGITIMIDADE PASSIVA']

merito = ['DA INAPLICABILIDADE DA LEI 8842/2020 – INCONSTITUCIONALIDADE',
          'DA CONSERVAÇÃO DO CONTRATO – “PACTA SUNT SERVANDA” – DO DEVIDO CUMPRIMENTO CONTRATUAL',
          'DA IMPOSSIBILIDADE DA INVERSÃO DO ÔNUS DA PROVA',
          'DA INEXISTÊNCIA DOS DANOS MORAIS PLEITEADOS',
          'DA ANÁLISE DA CONDUTA DA VÍTIMA',
          'DA INEXISTENCIA DE DANOS MATERIAIS']

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
    print('Preliminar não encontrada.')
