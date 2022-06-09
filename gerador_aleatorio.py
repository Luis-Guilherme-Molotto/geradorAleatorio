from math import pow as Pow
from typing import List


class GeradorAleatorio:
    tamanho: int
    semente: int
    multiplicador: int
    incremento: int
    modulo: int
    numeros_gerados: list[int] = []

    def __init__(
        self,
        tamanho: int = 20,
        semente: int = 1000,
        multiplicador: int = 8404997,
        incremento: int = 1,
        modulo: int = Pow(2, 35),
    ) -> None:
        self.tamanho = tamanho
        self.semente = semente
        self.multiplicador = multiplicador
        self.incremento = incremento
        self.modulo = modulo
        self.numeros_gerados.append(semente)

    def __calc_numero_aleatorio(self, valor_anterior: int) -> int:
        num_aleatorio = (
            self.multiplicador * valor_anterior + self.incremento
        ) % self.modulo

        return int(num_aleatorio)

    def exec(self) -> List[int]:
        for i in range(self.tamanho - 1):
            numero_aleatorio = self.__calc_numero_aleatorio(self.numeros_gerados[i])
            self.numeros_gerados.append(numero_aleatorio)

        return self.numeros_gerados
