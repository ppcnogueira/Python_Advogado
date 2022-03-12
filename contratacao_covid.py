# Controle de processos estratégicos
# Cuidado ao executar esta célula pois reseta o número de processos nas listas!!!!

# Meses/Semanas para controle / Inserir em cada lista a númeração dos processos
mês_semana1 = []
mês_semana2 = []
mês_semana3 = []
mês_semana4 = []

# Utilizar o for para verificar o total de processos recebidos na respectiva semana
i = i2 = i3 = i4 = 0

for processo in mês_semana1:
    i = i + 1
for processo in mês_semana2:
    i2 = i2 + 1
for processo in mês_semana3:
    i3 = i3 + 1
for processo in mês_semana4:
    i4 = i4 + 1

# Inserir neste input os processos recebidos
mês_semana1.append(str(input('Digite o número do processo recebido: ')))
for processo in mês_semana1:
  i2 = i2 + 1

print(f'Recebemos na 1º semana de Outubro {i} processos.')
print(f'Recebemos na 2º semana de Outubro {i2} processos.')
print(f'Recebemos na 3º semana de Outubro {i3} processos.')
print(f'Recebemos na 4º semana de Outubro {i4} processos.')
print(f'Recebemos em Outubro um total de {i + i2 + i3 + i4} processos.')
