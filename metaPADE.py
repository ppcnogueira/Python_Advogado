# Calcular meta do PADE Indenizatória 2020

def calc_meta(base_geral, base_acordo, base_imp=4424-518):
  print('*' * 30)
  print(f'---Improcedência---\nMeta 100%: {base_imp * 0.017:.1f} processos\nMeta 80%: {base_imp * 0.015:.1f} processos\nMeta 50%: {base_imp * 0.010:.1f} processos\nMeta 20%: {base_imp * 0.005:.1f} processos')
  print('*' * 30)
  print(f'---Acordos indenizatória---\nMeta 100%: {base_acordo * 0.091:.1f} processos\nMeta 75%: {base_acordo * 0.070:.1f} processos\nMeta 50%: {base_acordo * 0.050:.1f} processos\nMeta 25%: {base_acordo * 0.002:.1f} processos')

calc_meta(4424, 101) # Informar base geral, base de acordo e exceção
