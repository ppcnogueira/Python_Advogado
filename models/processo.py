
class Processo:
    contador: int = 1

    def __init__(self: object, numero_proc: str, parte_autora: str, uf: str) -> None:
        self.__codigo: int = Processo.contador
        self.__numero_proc: str = numero_proc
        self.__parte_autora: str = parte_autora
        self.__uf: str = uf
        Processo.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def num_processo(self: object) -> str:
        return self.__numero_proc

    @property
    def parte_autora(self: object) -> str:
        return self.__parte_autora

    @property
    def uf(self: object) -> str:
        return self.__uf

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNúmero do processo: {self.num_processo} \nParte Autora: {self.parte_autora} \nUF: {self.uf}'

