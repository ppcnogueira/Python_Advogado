from typing import List, Dict
from time import sleep
from models.processo import Processo


base: List[Dict[Processo, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=======================================================')
    print('=========== Sistema de controle de processos ==========')
    print('=====================  TESTEJUDI   ====================')
    print('=======================================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar processo')
    print('2 - Consultar processo')
    print('3 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_processo()
    elif opcao == 2:
        consultar_processo()
    elif opcao == 3:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_processo() -> None:
    print('Cadastro de Processo')
    print('===================')

    num_proc: str = input('Informe o número do processo: ')
    pautora: str = input('Informe o nome da parte autora: ')
    nova_uf: str = input('Digite a UF do processo: ')

    processo = Processo(num_proc, pautora, nova_uf)

    base.append(processo)

    print(f'O processo de nº {num_proc} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def consultar_processo() -> None:
        if len(base) > 0:
            print('Listagem de processo')
            print('--------------------')
            for processo in base:
                print(processo)
                print('----------------')
                sleep(1)
        else:
            print('Ainda não existem processos cadastrados.')
        sleep(2)
        menu()

def pega_processo_por_codigo(codigo: int) -> Processo:
    p: Processo = None

    for processo in base:
        if processo.codigo == codigo:
            p = processo
    return p

if __name__ == '__main__':
    main()

