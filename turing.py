import numpy as np
from abc import *
import logging

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
    def __init__(self, tasma, alfabet, symbol_pusty, stany, stan_poczatkowy, przejscia):
        self.tasma = tasma
        self.alfabet = alfabet 
        self.symbol_pusty = symbol_pusty
        self.stany = stany
        self.stan_poczatkowy = stan_poczatkowy
        self.przejscia = przejscia
    
    def RozpocznijDzialanieZmodyfikowanejTasmy(self, tasma):
        pass
    
    def RozpocznijDzialanieBEZZmodyfikowanejTasmy(self, tasma):
        for i in range(len(tasma)):
            for j in range(len(MaszynaTuringa.alfabet)):
                if tasma[i] != MaszynaTuringa.alfabet[j]:
                    print("zła tasma")
                    print(logging.FATAL)
                    break
        pass
    
    def CzyStanPoczątkowy(self, stan):
        pass
    
    def CzyStanKoncowy(self, stan):
        pass
    def WykonajKrok(self):
        pass
    def doznaku(self, tasma, indeks, znakibrake, oILE, kierunek): #kierunek -1 => lewo; 1 => prawo 
        a = 0
        for i in range(oILE):
            for n in range(len(znakibrake)):
                if tasma[indeks] == znakibrake[n]:
                    a = 1
                    break
            if a != 1: indeks += kierunek
        return tasma

    def zamiana(self, tasma, indeks, znakPocz, znakKonc, kierunek):
        if znakPocz == tasma[indeks]: 
            tasma[indeks] = znakKonc
            indeks += kierunek 
            return tasma
        else:
            print("Error - zamiana")
            print(logging.FATAL)
    def petlaZamian(self, indeks, K, kierunek):
        for i in range(K): #liczba cyfr
            indeks += kierunek
        return indeks
    
if __name__ == "__main__":
    alfabet = [0,1,2,3,4,5,6,7,8,9, ',','-', 'X']
    symbol_pusty = 'A'
    tasma = ['A',1,0,-0,5,'A']
    stan_poczatkowy = 0 
    Masz = MaszynaTuringa(123, 123 , 123, 123, 123)
    