# Calcular meta específicas

class CalculaMeta:

  # Atributo da classe CalculaMeta
  excecao=0  

  def __init__(self, base=0, base_acordo=0):    
    self.base = base
    self.base_acordo = base_acordo

    # Cálculo de 100% da meta de improcedência
    self.metaimp = (base-CalculaMeta.excecao) * 0.017

    # Cálculo de 100% da meta de outros motivos
    self.metageral = base * 0.0149

    # Cálculo de 100% da meta de acordos
    self.metaacordo = base_acordo * 0.091

# Variáveis para informar o número das bases
improcedencia = CalculaMeta('Informar aqui o número da base de processos')
acordos = CalculaMeta(base_acordo='Informar o número da base de acordos')
outros = CalculaMeta('Informar aqui o número da base de processos')

# Resultado
print(f'META DE IMPROCEDÊNCIA: {improcedencia.metaimp:.1f}')
print(f'META DE ACORDO: {acordos.metaacordo:.1f}')
print(f'META DE OUTROS MOTIVOS: {outros.metageral:.1f}')
