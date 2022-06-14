from math import sqrt
from typing import List

from teste_ks import TesteKS

# Teste de uniformidade utilizando Kolmogorov-Smirnov


class TesteUniformidade(TesteKS):
    def __init__(self, classes: int = 20, precisao: int = 12) -> None:
        self._classes = classes
        super().__init__(precisao=precisao)

    def _calc_li(self):
        return [i / self._classes for i in range(self._classes)]

    def _calc_ls(self):
        return [(i + 1) / self._classes for i in range(self._classes)]

    def _calc_fo(self, numeros: List[float], li: List[float], ls: List[float]):
        fo = [0 for i in range(self._classes)]

        for numero in numeros:
            for index in range(self._classes):
                if numero > li[index] and numero <= ls[index]:
                    fo[index] += 1
        return fo

    def exec(self, numeros: List[float]):
        li = self._calc_li()
        ls = self._calc_ls()
        fo = self._calc_fo(numeros, li, ls)
        pi = self._calc_pi(fo)
        gx = self._calc_gx(pi)
        fx = ls

        teste = self._calc_teste(fx, gx)
        ks = self._calc_ks(teste)
        ks5 = self._calc_ks5(numeros)

        print("Aceita H0: Os valores observados tem distribuicao uniforme" if ks < ks5 else "Rejeita H0: Os valores observados nao tem distribuicao uniforme")
        #print(ks)
        #print(ks5)
