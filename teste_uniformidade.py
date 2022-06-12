from math import sqrt
from typing import List

from teste_ks import TesteKS

# Teste de uniformidade utilizando Kolmogorov-Smirnov


class TesteUniformidade(TesteKS):
    def __init__(self, classes: int = 20, precisao: int = 12) -> None:
        self._classes = classes
        self._precisao = precisao

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

    def _calc_pi(self, numeros: List[float], fo: List[float]):
        len_numeros = len(numeros)
        return [fo[i] / len_numeros for i in range(self._classes)]

    def _calc_gx(self, pi: List[float]):
        gx = [pi[0]]
        len_pi = len(pi)

        for i in range(len_pi - 1):
            gx.append(round((gx[i] + pi[i + 1]), self._precisao))

        return gx

    def _calc_teste(self, fx: List[float], gx: List[float]):
        return [
            abs(round((fx[i] - gx[i]), self._precisao)) for i in range(self._classes)
        ]

    def exec(self, numeros: List[float]):
        li = self._calc_li()
        ls = self._calc_ls()
        fo = self._calc_fo(numeros, li, ls)
        pi = self._calc_pi(numeros, fo)
        gx = self._calc_gx(pi)
        fx = ls

        teste = self._calc_teste(fx, gx)
        ks = max(teste)
        ks5 = 1.36 / sqrt(len(numeros))

        print("Aceita H0" if ks < ks5 else "Rejeita H0")
        print(ks)
        print(ks5)
