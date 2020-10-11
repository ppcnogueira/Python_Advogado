# Calcular meta do PADE Indenizatória 2020
base_geral = 4424
base_acordo = 101

# Diminuir do número informado o total de processos de execução fiscal e planos eoconômicos
base_imp = base_geral - 518
print('*' * 60)
print(f'---Improcedência---\nMeta 100%: {base_imp * 0.017:.1f} processos\nMeta 80%: {base_imp * 0.015:.1f} processos\nMeta 50%: {base_imp * 0.010:.1f} processos\n'
      f'Meta 20%: {base_imp * 0.005:.1f} processos')
print('*' * 60)
print(f'---Acordos indenizatória---\nMeta 100%: {base_acordo * 0.091:.1f} processos\nMeta 75%: {base_acordo * 0.070:.1f} processos\nMeta 50%: {base_acordo * 0.050:.1f}'
      f' processos\nMeta 25%: {base_acordo * 0.002:.1f} processos')
