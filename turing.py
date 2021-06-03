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
    # @abstractmethod
    # def RozpocznijDzialanieBEZZmodyfikowanejTasmy(self, tasma):
    #     pass
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
    def __init__(self, tasma, alfabet, symbol_pusty, stany, stan_poczatkowy, przejscia, ilecyfr):
        self.tasma = tasma
        self.alfabet = alfabet 
        self.symbol_pusty = symbol_pusty
        self.stany = stany
        self.stan_poczatkowy = stan_poczatkowy
        self.przejscia = przejscia
        self.ilecyfr = ilecyfr
    
    def RozpocznijDzialanieZmodyfikowanejTasmy(self, tasma):
        pass
    
    def CzyStanPoczątkowy(self, stan):
        if stan != MaszynaTuringa.stan_poczatkowy:
            return 0
        else:
            return 1
    
    def CzyStanKoncowy(self, stan):
        pass
    def WykonajKrok(self):
        pass
    def doznaku(self, tasma, indeks, znakibrake, kierunek): #kierunek -1 => lewo; 1 => prawo 
        a = 1
        while(a):
            indeks += kierunek
            for n in range(len(znakibrake)):
                if tasma[indeks] == znakibrake[n]:
                    a = 0
                    break
        return indeks 

    def zamiana(self, tasma, indeks, znakPocz, znakKonc, kierunek):
        if znakPocz == tasma[indeks]: 
            tasma[indeks] = znakKonc
            indeks += kierunek 
            return [tasma,indeks]
        else:
            print("Error - zamiana")
            print(logging.FATAL)
    def petlaZamian(self, indeks, K, kierunek):
        for i in range(K): #liczba cyfr z przecinkiem
            indeks += kierunek
        return indeks
    def RozpocznijDzialanieTasmy(self, tasma):
        for i in range(len(tasma)):
            for j in range(len(self.alfabet)):
                if tasma[i] != self.alfabet[j]:
                    print("zła tasma")
                    print(logging.FATAL)
                    break
        indeks = 0 
        tasma, indeks = self.q0(tasma,indeks)
        dzialanie = 1
        while(dzialanie):
            indeks = self.q1(tasma, indeks)
            print(1)
            tasma, indeks, zmienna, koniec = self.q2(tasma, indeks)
            if koniec == 1: dzialanie = 0 
            tasma, indeks = self.q_n(tasma, indeks, zmienna)
            indeks = self.Q1(tasma, indeks)
        print(tasma,indeks)

    def q0(self, tasma, indeks):
        indeks = 0 
        tasma,indeks = self.zamiana(tasma, indeks, 'A', 'A', 1)
        return [tasma, indeks]
    def q1(self, tasma, indeks):
        indeks = self.doznaku(tasma, indeks, ['X','A'], 1)
        indeks -= 1 
        return indeks
    def q2(self, tasma, indeks):
        koniec = 0
        zmienna = tasma[indeks]
        if zmienna == '-':
            koniec = 1 
            return [tasma, indeks, zmienna, koniec]
        else:
            tasma[indeks] = 'X'
            return [tasma, indeks, zmienna, koniec]
    def q_n(self, tasma, indeks, zmiennaprawa):
        indeks = self.petlaZamian(indeks, self.ilecyfr - 1, -1)
        zmiennalewa = tasma[indeks]
        print(zmiennalewa)
        if zmiennalewa >= zmiennaprawa:
            tasma[indeks] = zmiennalewa - zmiennaprawa
            indeks +- 1 
        else:
            tasma[indeks] = 10 + zmiennalewa - zmiennaprawa
            indeks -= 1
            while(True):
                if tasma[indeks] == 0:
                    tasma[indeks] = 9
                    indeks -= 1 
                else:
                    tasma[indeks] -= 1 
                    indeks -= 1 
                    break
        return[tasma, indeks]
    def Q1(self, tasma, indeks):
        indeks = self.doznaku(tasma,indeks, 'A', -1)
        indeks += 1

if __name__ == "__main__":
    alfabet = [0,1,2,3,4,5,6,7,8,9, ',','-', 'X']
    symbol_pusty = 'A'
    tasma = ['A',1,0,'-',0,5,'A']
    stan_poczatkowy = 0 
    Masz = MaszynaTuringa(tasma, alfabet,symbol_pusty,123, stan_poczatkowy, 123, len(tasma) - 1)
    Masz.RozpocznijDzialanieTasmy(tasma)