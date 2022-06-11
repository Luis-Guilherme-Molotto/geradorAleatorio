from abc import ABC, abstractmethod
from typing import List


class TesteKS(ABC):
    @abstractmethod
    def _calc_fo(self, li: List[float], ls: List[float]) -> List[float]:
        pass

    @abstractmethod
    def _calc_pi(self, fo: List[float]) -> List[float]:
        pass

    @abstractmethod
    def _calc_gx(self, pi: List[float]) -> List[float]:
        pass

    @abstractmethod
    def _calc_teste(self, fx: List[float], gx: List[float]) -> List[float]:
        pass
