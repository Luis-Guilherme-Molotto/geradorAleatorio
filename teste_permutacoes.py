from operator import length_hint
from typing import List
from math import factorial, sqrt
from teste_ks import TesteKS


class TestePermutacoes(TesteKS):
    def __init__(self, precisao=12) -> None:
        super().__init__(precisao=precisao)

    def _calc_fo(self, numeros: List[float]):
        contador = 0
        fo: List[int] = [0, 0, 0, 0, 0, 0]
        tamanho = len(numeros)/3

        for i in range(0, int(tamanho)):
            numero_1 = numeros[contador]
            numero_2 = numeros[contador + 1]
            numero_3 = numeros[contador + 2]
            
            if numero_1 < numero_2 and numero_2 < numero_3:
                fo[0] = fo[0] + 1
            elif numero_1 < numero_3 and numero_3 < numero_2:
                fo[1] = fo[1] + 1
            elif numero_2 < numero_1 and numero_1 < numero_3:
                fo[2] = fo[2] + 1
            elif numero_2 < numero_3 and numero_3 < numero_1:
                fo[3] = fo[3] + 1
            elif numero_3 < numero_1 and numero_1 < numero_2:
                fo[4] = fo[4] + 1
            elif numero_3 < numero_2 and numero_2 < numero_1:
                fo[5] = fo[5] + 1

            contador = contador + 3

        return fo

    def _calc_px(self, tamanho):
        px = [1 / factorial(3) for i in range(tamanho)]

        return px

    def _calc_fx(self, px: List[float]):
        return self._soma_acumulada(px)

    def exec(self, numeros: List[float], tipo: str = "asc"):
        fo = self._calc_fo(numeros)

        pi = self._calc_pi(fo)

        gx = self._calc_gx(pi)

        px = self._calc_px(len(fo))

        fx = self._calc_fx(px)

        teste = self._calc_teste(fx, gx)

        ks = self._calc_ks(teste)
        ks5 = self._calc_ks5_permutacao(numeros)

        print("Aceita H0: Os ordenamentos observados nao diferem dos esperados" if ks < ks5 else "Rejeita H0: Os ordenamentos observados diferem dos esperados")
        print(ks)
        print(ks5)
