import numpy as np
from abc import *

class AbstrackMaszynaTuringa(ABC):
    @abstractmethod
    def __init__(self, alfabet, symbol_pusty, stany, stan_początkowy, przejscia):
        pass
    @abstractmethod
    def RozpocznijDzialanieZmodyfikowanejTasmy(self,tasma):
        pass
    @abstractmethod
    def RozpocznijDzialanieBEZZmodyfikowanejTasmy(self, tasma):
        pass
    @abstractmethod
    def CzyStanPoczątkowy(self, stan):
        pass
    @abstractmethod
    def CzyStanKoncowy(self, stan):
        pass
    @abstractmethod
    def WykonajKrok(self):
        pass
class MaszynaTuringa(AbstrackMaszynaTuringa):
    def __init__(self, alfabet, symbol_pusty, stany, stan_poczatkowy, przejscia):
        self.alfabet = alfabet 
        self.symbol_pusty = symbol_pusty
        self.stany = stany
        self.stan_poczatkowy = stan_poczatkowy
        self.przejscia = przejscia
    
    def RozpocznijDzialanieZmodyfikowanejTasmy(self, Tasma):
        pass
    
    def RozpocznijDzialanieBEZZmodyfikowanejTasmy(self, Tasma):
        pass
    
    def CzyStanPoczątkowy(self, stan):
        pass
    
    def CzyStanKoncowy(self, stan):
        pass
    def WykonajKrok(self):
        pass


if __name__ == "__main__":
    alfabet = [0,1,2,3,4,5,6,7,8,9, ',','-']
    symbol_pusty = '#'
    Masz = MaszynaTuringa(123, 123 , 123, 123, 123)
    