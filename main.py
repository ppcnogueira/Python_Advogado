import tkinter as tk
from tkinter import ttk

def obrigacao_fazer():
    data_solicitacao = entry_data_solicitacao.get()
    obrigacao = entry_obrigacao.get()
    forma_detalhada = entry_forma_detalhada.get()
    opcao = opcao_var.get()
    tipo_contrato = entry_tipo_contrato.get()
    num_contrato = entry_num_contrato.get()
    valortotal_contrato = entry_valortotal_contrato.get()
    valorparcela_contrato = entry_valorparcela_contrato.get()
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    agencia = entry_agencia.get()
    conta = entry_conta.get()
    prazo_cumprimento = entry_prazo_cumprimento.get()
    prazo_inicio = entry_prazo_inicio.get()
    prazo_fim = entry_prazo_inicio.get()
    multa = entry_multa.get()


    if opcao == "Cartões":
        resultado = f"Data da intimação: {data_solicitacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nTipo de contrato: {tipo_contrato}\nNúmero do contrato: {num_contrato}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"
        resultado_label.config(text=resultado)
    elif opcao == "Empréstimo":
        resultado = f"Data da intimação: {data_solicitacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nTipo de contrato: {tipo_contrato}\nNúmero do contrato: {num_contrato}\nValor total do contrato: {valortotal_contrato}\nValor da parcela: {valorparcela_contrato}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"

    else:
        resultado = f"Data da intimação: {data_solicitacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nAgencia e conta ligada ao contrato: {agencia}| {conta}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"

# Cria a janela principal
janela = tk.Tk()
janela.title("Formulário com Resultado na Tela")

# Cria rótulos e entradas para o formulário
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

# Menu suspenso (combobox)
opcoes = ["Opção 1", "Opção 2", "Opção 3"]
opcao_var = tk.StringVar()
label_opcao = tk.Label(janela, text="Escolha uma opção:")
label_opcao.pack()
opcao_combobox = ttk.Combobox(janela, textvariable=opcao_var, values=opcoes)
opcao_combobox.pack()

# Botão para calcular o resultado
botao_calcular = tk.Button(janela, text="Calcular Resultado", command=obrigacao_fazer)
botao_calcular.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicia a interface gráfica
janela.mainloop()

