# PROGRAMA PARA VERIFICAR AS DEFESAS DE SUSPENSÃO/PRORROGAÇÃO - COVID

defesa = (input('Cole aqui a contestação: '))

# Tópicos que serão verificados
preliminar = ['DA INCONSTITUCIONALIDADE DA LEI 8842/2020 - ADI 6495', 'DA INCONSTITUCIONALIDADE DA LEI LOCAL 2.472/2020']
ilegitimidade = 'DA ILEGITIMIDADE PASSIVA'
merito = ['DA INAPLICABILIDADE DA LEI 8842/2020 – INCONSTITUCIONALIDADE', 'DA CONSERVAÇÃO DO CONTRATO – “PACTA SUNT SERVANDA” – DO DEVIDO CUMPRIMENTO CONTRATUAL',
          'DA IMPOSSIBILIDADE DA INVERSÃO DO ÔNUS DA PROVA', 'DA INEXISTÊNCIA DOS DANOS MORAIS PLEITEADOS', 'DA ANÁLISE DA CONDUTA DA VÍTIMA', 'DA INEXISTENCIA DE DANOS MATERIAIS']

# Checagem na variável 'defesa' se os tópicos informados acima estão presentes
print()
if preliminar[0] or preliminar[1] in defesa: 
  print('Tópico de INCONSTITUCIONALIDADE DA LEI 8842/2020 ou 2472/2020 [OK]')
else:
  print('Está faltando o tópico de INCONSTITUCIONALIDADE DA LEI 8842/2020')

print('='*30)

if ilegitimidade in defesa:
  print('Tópico de DA ILEGITIMIDADE PASSIVA [OK]')
else:
  print('Está faltando o tópico de DA ILEGITIMIDADE PASSIVA')

print('='*30)

if merito[0] in defesa:
  print(f'Tópico {merito[0]}: [OK]')
else:
  print('O mérito não está completo.')

if merito[1] in defesa:
  print(f'Tópico {merito[1]}: [OK]')
else:
  print('O mérito não está completo.')

if merito[2] in defesa:
  print(f'Tópico {merito[2]}: [OK]')
else:
  print('O mérito não está completo.')

if merito[3] in defesa:
  print(f'Tópico {merito[3]}: [OK]')
else:
  print('O mérito não está completo.')

if merito[4] in defesa:
  print(f'Tópico {merito[4]}: [OK]')
else:
  print('O mérito não está completo.')

print('='*30)

# Checagem do tópico de danos materiais
if merito[5] in defesa:
  print(f'Tópico {merito[5]}: [OK]')
else:
  print('Tópico de DANO MATERIAL não encontrado. Verificar na inicial se há pedido sobre dano material')
