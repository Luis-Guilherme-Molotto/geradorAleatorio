from abc import ABC, abstractmethod
from math import sqrt
from typing import List


class TesteKS(ABC):
    def __init__(self, precisao: int = 12) -> None:
        self._precisao = precisao

    @abstractmethod
    def _calc_fo(self, li: List[float], ls: List[float]) -> List[float]:
        pass

    def _soma_acumulada(self, lista: List[float]):
        soma_acc = [lista[0]]

        for i in range(len(lista) - 1):
            soma_acc.append(round((soma_acc[i] + lista[i + 1]), self._precisao))

        return soma_acc

    def _calc_pi(self, fo: List[float]) -> List[float]:
        fo_soma = sum(fo)

        return [freq_observ / fo_soma for freq_observ in fo]

    def _calc_gx(self, pi: List[float]) -> List[float]:
        return self._soma_acumulada(pi)

    def _calc_teste(self, fx: List[float], gx: List[float]) -> List[float]:
        if len(fx) != len(gx):
            raise Exception("parametros de _calc_teste invalidos")

        return [abs(round((fx[i] - gx[i]), self._precisao)) for i in range(len(fx))]

    def _calc_ks(self, teste: List[float]) -> float:
        return max(teste)

    def _calc_ks5(self, numeros: List[float]) -> float:
        return 1.36 / sqrt(len(numeros))
