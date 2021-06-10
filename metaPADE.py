# Calcular meta do PADE Indenizatória 2021
class CalculaMeta:

  def __init__(self, base=5501, base_acordo=170, excecao=680):    
    self.base = base
    self.base_acordo = base_acordo
    self.excecao = excecao

    # Cálculo de 100% da meta de improcedência
    self.metaimp = (base - excecao) * 0.018

    # Cálculo de 100% da meta de outros motivos
    self.metaoutros = (base - excecao) * 0.017

    # Cálculo de 100% da meta de sem custos
    self.metasemcusto = (base - excecao) * 0.017

    # Cálculo de 100% da meta de acordos
    self.metaacordo = base_acordo * 0.091


class CalculaMetaTrab:

  def __init__(self, base=1669):    
    self.base = base

# Cálculo da meta de improcedência
    self.metaimptotal = base * 0.017
    self.metaimp80 = base * 0.014
    self.metaimp50 = base * 0.006
    self.metaimp20 = base * 0.001

    # Cálculo de 100% da meta de outros motivos
    self.metaoutrostotal = base * 0.015
    self.metaoutros80 = base * 0.010
    self.metaoutros50 = base * 0.001

    # Cálculo da meta de acordos
    self.metaacordototal = base * 0.017
    self.metaacordo80 = base * 0.014
    self.metaacordo50 = base * 0.006
    self.metaacordo20 = base * 0.001


# Variáveis para informar o número das bases
improcedencia = CalculaMeta()
acordos = CalculaMeta()
outros = CalculaMeta()

trabimprocedencia = CalculaMetaTrab(1669)
trabacordos = CalculaMetaTrab(1669)
traboutros = CalculaMetaTrab(1669)

# Resultado
print('Metas Indenizatória')
print(f'Meta de Improcedência: {improcedencia.metaimp:.1f} processos')
print(f'Meta de Acordo: {acordos.metaacordo:.1f} processo')
print(f'Meta de encerramento por outros motivos: {outros.metaoutros:.1f} processos')
print(f'Meta de encerramento de processos sem custo: {outros.metasemcusto:.1f} processos\n')
print('Metas Trabalhista\n')
print(f'Meta de Improcedência 100%: {trabimprocedencia.metaimptotal:.1f} processos')
print(f'Meta de Improcedência 80%: {trabimprocedencia.metaimp80:.1f} processos')
print(f'Meta de Improcedência 50%: {trabimprocedencia.metaimp50:.1f} processos')
print(f'Meta de Improcedência 20%: {trabimprocedencia.metaimp20:.1f} processos\n')
print(f'Meta de Acordos 100%: {trabacordos.metaacordototal:.1f} processos')
print(f'Meta de Acordos 80%: {trabacordos.metaacordo80:.1f} processos')
print(f'Meta de Acordos 50%: {trabacordos.metaacordo50:.1f} processos')
print(f'Meta de Acordos 20%: {trabacordos.metaacordo20:.1f} processos\n')
print(f'Meta de Outros Motivos 100%: {traboutros.metaoutrostotal:.1f} processos')
print(f'Meta de Outros Motivos 80%: {traboutros.metaoutros80:.1f} processos')
print(f'Meta de Outros Motivos 50%: {traboutros.metaoutros50:.1f} processos')

