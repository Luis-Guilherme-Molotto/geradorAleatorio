from math import sqrt
from typing import List

# Teste de uniformidade utilizando Kolmogorov-Smirnov


class TesteUniformidade:
    def __init__(
        self, numeros: List[float], classes: int = 20, precisao: int = 12
    ) -> None:
        self._numeros = numeros
        self._classes = classes
        self._precisao = precisao

    def _calc_normalizador(self):
        return 10 ** self._precisao

    def _calc_li(self):
        return [i / self._classes for i in range(self._classes)]

    def _calc_ls(self):
        return [(i + 1) / self._classes for i in range(self._classes)]

    def _calc_fo(self, li: List[float], ls: List[float]):
        fo = [0 for i in range(self._classes)]

        for numero in self._numeros:
            for index in range(self._classes):
                limite_inferior = li[index]
                limite_superior = ls[index]
                if numero > limite_inferior and numero <= limite_superior:
                    fo[index] += 1
        return fo

    def _cacl_pi(self, fo: List[float]):
        len_numeros = len(self._numeros)
        return [fo[i] / len_numeros for i in range(self._classes)]

    def _calc_gx(self, pi: List[float]):
        norm = self._calc_normalizador()
        gx = [pi[0]]

        len_pi = len(pi)
        for i in range(len_pi - 1):
            gx.append((norm * gx[i] + norm * pi[i + 1]) / norm)

        return gx

    def _calc_teste(self, fx: List[float], gx: List[float]):
        norm = self._calc_normalizador()
        return [abs((norm * fx[i] - norm * gx[i]) / norm) for i in range(self._classes)]

    def exec(self):
        li = self._calc_li()
        ls = self._calc_ls()
        fo = self._calc_fo(li, ls)
        pi = self._cacl_pi(fo)
        gx = self._calc_gx(pi)
        fx = ls

        teste = self._calc_teste(fx, gx)
        ks = max(teste)
        ks5 = 1.36 / sqrt(len(self._numeros))

        print("Aceita H0" if ks < ks5 else "Rejeita H0")
