import tkinter as tk
from tkinter import ttk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def obrigacao_fazer():
    data_intimacao = entry_data_intimacao.get()
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
        resultado = f"Data da intimação: {data_intimacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nTipo de contrato: {tipo_contrato}\nNúmero do contrato: {num_contrato}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"
        resultado_label.config(text=resultado)
    elif opcao == "Empréstimo":
        resultado = f"Data da intimação: {data_intimacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nTipo de contrato: {tipo_contrato}\nNúmero do contrato: {num_contrato}\nValor total do contrato: {valortotal_contrato}\nValor da parcela: {valorparcela_contrato}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"

    else:
        resultado = f"Data da intimação: {data_intimacao}\nRegistrar a obrigação imposta: {obrigacao}\nForma detalhada para cumprimento:\n {forma_detalhada}\nAgencia e conta ligada ao contrato: {agencia}| {conta}\nNome: {nome}\nCpf: {cpf}\nPrazo para cumprimento: {prazo_cumprimento}\nData do início do prazo: {prazo_inicio}\nData do fim do prazo: {prazo_fim}\nMulta: {multa}"

# Cria a janela principal
janela = tk.Tk()
janela.title("Formulário de obrigação de fazer")
window_width = 400
window_height = 800

# Cria rótulos e entradas para o formulário
label_data_intimacao = tk.Label(janela, text="Data da intimação:")
label_data_intimacao.pack()
entry_data_intimacao = tk.Entry(janela)
entry_data_intimacao.pack()

label_obrigacao = tk.Label(janela, text="Obrigação estabelecida:")
label_obrigacao.pack()
entry_obrigacao = tk.Entry(janela)
entry_obrigacao.pack()

label_forma_detalhada = tk.Label(janela, text="Forma detalhada para cumprimento:")
label_forma_detalhada.pack()
entry_forma_detalhada = tk.Entry(janela)
entry_forma_detalhada.pack()

# Menu suspenso (combobox)
opcoes = ["Opção 1", "Opção 2", "Opção 3"]
opcao_var = tk.StringVar()
label_opcao = tk.Label(janela, text="Escolha uma opção:")
label_opcao.pack()
opcao_combobox = ttk.Combobox(janela, textvariable=opcao_var, values=opcoes)
opcao_combobox.pack()

label_tipo_contrato = tk.Label(janela, text="Tipo de contrato:")
label_tipo_contrato.pack()
entry_tipo_contrato = tk.Entry(janela)
entry_tipo_contrato.pack()

label_num_contrato = tk.Label(janela, text="Número do contrato:")
label_num_contrato.pack()
entry_num_contrato = tk.Entry(janela)
entry_num_contrato.pack()

label_valortotal_contrato = tk.Label(janela, text="Valor total do contrato:")
label_valortotal_contrato.pack()
entry_valortotal_contrato = tk.Entry(janela)
entry_valortotal_contrato.pack()

label_valorparcela_contrato = tk.Label(janela, text="Valor da parcela do contrato:")
label_valorparcela_contrato.pack()
entry_valorparcela_contrato = tk.Entry(janela)
entry_valorparcela_contrato.pack()

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_cpf = tk.Label(janela, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(janela)
entry_cpf.pack()

label_agencia = tk.Label(janela, text="Agencia:")
label_agencia.pack()
entry_agencia = tk.Entry(janela)
entry_agencia.pack()

label_conta = tk.Label(janela, text="Conta:")
label_conta.pack()
entry_conta = tk.Entry(janela)
entry_conta.pack()

label_prazo_cumprimento = tk.Label(janela, text="Prazo para cumprimento:")
label_prazo_cumprimento.pack()
entry_prazo_cumprimento = tk.Entry(janela)
entry_prazo_cumprimento.pack()

label_prazo_inicio = tk.Label(janela, text="Data inicial do prazo:")
label_prazo_inicio.pack()
entry_prazo_inicio = tk.Entry(janela)
entry_prazo_inicio.pack()

label_prazo_fim = tk.Label(janela, text="Data final do prazo:")
label_prazo_fim.pack()
entry_prazo_fim = tk.Entry(janela)
entry_prazo_fim.pack()

label_multa = tk.Label(janela, text="Multa:")
label_multa.pack()
entry_multa = tk.Entry(janela)
entry_multa.pack()

# Botão para calcular o resultado
botao_calcular = tk.Button(janela, text="Calcular Resultado", command=obrigacao_fazer)
botao_calcular.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicia a interface gráfica
center_window(janela, window_width, window_height)
janela.mainloop()
