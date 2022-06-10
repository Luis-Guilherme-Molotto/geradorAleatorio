from math import pow as Pow


class GeradorAleatorio:
    def __init__(
        self,
        tamanho: int = 20,
        semente: int = 1000,
        multiplicador: int = 8404997,
        incremento: int = 1,
        modulo: int = Pow(2, 35),
    ) -> None:
        self._tamanho = tamanho
        self._semente = semente
        self._multiplicador = multiplicador
        self._incremento = incremento
        self._modulo = modulo

    def __calc_numero_aleatorio(self, valor_anterior: int):
        num_aleatorio = (
            self._multiplicador * valor_anterior + self._incremento
        ) % self._modulo

        return int(num_aleatorio)

    def exec(self):
        numero_anterior = self._semente
        valores_aleatorios: list[float] = []
        for i in range(self._tamanho - 1):
            numero_anterior = self.__calc_numero_aleatorio(numero_anterior)
            valores_aleatorios.append(numero_anterior / self._modulo)

        return valores_aleatorios
