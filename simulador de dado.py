# Simulador de dado
# Gerar um valor de 1 até 6

from random import randint
import random
from typing import Text
import PySimpleGUI as sg


# Definir o nome da classe e os dados iniciais do programa
class SimuladorDeDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # Criar uma Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.ValordoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não.')
        except:
            print('Ocorreu um erro ao receber sua resposta.')

    def ValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDados()
simulador.Iniciar()