from operator import length_hint
from typing import List
from math import factorial, sqrt
import math
from matplotlib.pyplot import prism
import numpy as np


from numpy import around
from teste_ks import TesteKS


class TesteIntervalo(TesteKS):
    def __init__(self, precisao=12) -> None:
        super().__init__(precisao=precisao)

    def _truncate(self, numero, casas):
        return math.floor(numero * 10 ** casas) / 10 ** casas

    def _calc_fo(self, numeros: List[float], d):
        contador = 0
        maximo = 0
        fo: List[int] = []

        for i in range(len(numeros)):
            num_trunc = self._truncate(numeros[i], 1)            

            if num_trunc != d/10:
                fo.append(0)
                contador = contador + 1
                if i == (len(numeros)-1):
                    fo.append(0)
                    fo[contador] = fo[contador] + 1
                    if contador > maximo:
                        maximo = contador
            else:
                fo.append(0)
                fo[contador] = fo[contador] + 1
                if contador > maximo:
                    maximo = contador
                if i == (len(numeros)-1):
                    fo.append(0)
                    fo[contador] = fo[contador] + 1
                    if contador > maximo:
                        maximo = contador
                contador = 0

        f0 = fo[0:maximo+1]
        return f0

    def _calc_px(self, tamanho):
        px = [0.9 ** i * 0.1 for i in range(tamanho)]

        return px

    def _calc_fx(self, px: List[float]):
        return self._soma_acumulada(px)

    def exec(self, numeros: List[float], d: int = 5):

        fo = self._calc_fo(numeros, d)

        pi = self._calc_pi(fo)

        gx = self._calc_gx(pi)

        px = self._calc_px(len(fo))

        fx = self._calc_fx(px)

        teste = self._calc_teste(fx, gx)

        ks = self._calc_ks(teste)
        ks5 = self._calc_ks5_intervalo(fo)

        print(f"Aceita H0: Os intervalos observados para {d} nao diferem dos esperados" if ks < ks5 else "Rejeita H0: Os intervalos observados para {d} diferem dos esperados")
        print(ks)
        print(ks5)