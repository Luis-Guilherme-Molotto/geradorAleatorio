from typing import List
from math import factorial, sqrt
from teste_ks import TesteKS


class TesteCorrida(TesteKS):
    def __init__(self, precisao=12) -> None:
        super().__init__(precisao=precisao)
        pass

    def _calc_fo(self, corrida: List[int], classes: List[int]):
        fo = [0 for _cls in classes]

        for cor in corrida:
            for index, cls in enumerate(classes):
                if cls == cor:
                    fo[index] += 1

        return fo

    def _calc_fx(self, classes: List[int]) -> List[float]:
        px = [cls / factorial(cls + 1) for cls in classes]

        return self._soma_acumulada(px)

    def _contar_corrida_asc(self, numeros: List[float]):
        contador = 1
        corrida: List[int] = []
        anterior_maior = False

        for i in range(1, len(numeros)):
            if numeros[i] > numeros[i - 1] or anterior_maior:
                contador += 1
                anterior_maior = False
            else:
                corrida.append(contador)
                contador = 0
                anterior_maior = True

        return corrida

    def _contar_corrida_desc(self, numeros: List[float]):
        contador = 1
        corrida: List[int] = []
        anterior_menor = False

        for i in range(1, len(numeros)):
            if numeros[i] < numeros[i - 1] or anterior_menor:
                contador += 1
                anterior_menor = False
            else:
                corrida.append(contador)
                contador = 0
                anterior_menor = True

        return corrida

    def _calc_classes(self, corrida: List[int]):
        corrida_max = max(corrida)
        return [num + 1 for num in range(corrida_max)]

    def _calc_corrida(self, numeros: List[float], tipo: str):
        if tipo == "asc":
            return self._contar_corrida_asc(numeros)
        
        if tipo == "desc":
            return self._contar_corrida_desc(numeros)

        raise Exception("tipo de corrrida invalida")

    def exec(self, numeros: List[float], tipo: str = "asc"):
        corrida = self._calc_corrida(numeros, tipo)
        classes = self._calc_classes(corrida)
        fo = self._calc_fo(corrida, classes)
        pi = self._calc_pi(fo)
        gx = self._calc_gx(pi)
        fx = self._calc_fx(classes)

        teste = self._calc_teste(fx, gx)
        ks = self._calc_ks(teste)
        ks5 = self._calc_ks5(numeros)

        print("Aceita H0" if ks < ks5 else "Rejeita H0")
        print(ks)
        print(ks5)
