# Controle de processos de Covid
# Cuidado ao executar esta célula pois reseta o número de processos nas listas!!!!

# Meses/Semanas para controle
outubro_1 = ['2000572909', '2000511220', '2000553197', '2000578039', '2000576949', '2000572909', '2000572815',
             '2000566766', '2000591286', '2000591010', '2000576774', '2000593839',
             '2000576708', '2000593477', '2000576821', '2000577073', '2000593051', '2000592926', '2000593607',
             '2000588052', '2000562164', ]
outubro_2 = []
outubro_3 = []
outubro_4 = []

# Utilizar o for para verificar o total de processos recebidos na respectiva semana
i = i2 = i3 = i4 = 0

for gcpj in outubro_1:
    # print(gcpj)
    i = i + 1
for gcpj in outubro_2:
    # print(gcpj)
    i2 = i2 + 1
for gcpj in outubro_3:
    # print(gcpj)
    i3 = i3 + 1
for gcpj in outubro_4:
    # print(gcpj)
    i4 = i4 + 1

# Inserir neste input os GCPJs recebidos
outubro_2.append(str(input('Digite o GCPJ recebido: ')))
for gcpj in outubro_2:
  #print(gcpj)
  i2 = i2 + 1

print(f'Recebemos na 1º semana de Outubro {i} processos.')
print(f'Recebemos na 2º semana de Outubro {i2} processos.')
print(f'Recebemos na 3º semana de Outubro {i3} processos.')
print(f'Recebemos na 4º semana de Outubro {i4} processos.')
print(f'Recebemos em Outubro um total de {i + i2 + i3 + i4} processos.')

# Verificar as listas

#print(outubro_1)
#print(outubro_2)
#print(outubro_3)
#print(outubro_4)