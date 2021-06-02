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
        self.head = 0
        self.stan_teraz = self.stan_poczatkowy
     
    def RozpocznijDzialanieZmodyfikowanejTasmy(self, tasma):
        pass
    def RozpocznijDzialanieBEZZmodyfikowanejTasmy(self, tasma):
        pass
    
    def CzyStanPoczątkowy(self, stan):
        return stan == self.stan_poczatkowy
    def CzyStanKoncowy(self, stan):
        return stan == 'end'
    #dajindex - zwraca na którym miejscu w poszczególnym stanie(liście) stany['q1'][^tu^] stoi dany znak | ^tu^- nie chcemy znaku tylko int indexu
    def DajIndex(self, stany, wCzymSzukamy, czegoSzukamy):
        i = 0 
        for i in range(len(self.stany[wCzymSzukamy])):
            if self.stany[wCzymSzukamy][i][0] == czegoSzukamy:
                return i

    def WykonajKrok(self):
        aktualnyZnak = self.tasma[self.head] # na tym znaku na taśmie teraz jestem
        stan_obecny = self.stan_teraz #w jakim stanie teraz jestem 

        #Zwraca następny stan 
        a = self.DajIndex(self.stany, stan_obecny, aktualnyZnak)
        nastepny_stan = self.stany[stan_obecny][a][3]

        #zamienia znak na tasmie i zmienia head, czyli położenie głowicy
        self.tasma[self.head] = self.stany[stan_obecny][a][1]
        self.head += self.stany[stan_obecny][a][2]
        #podmienia stan
        self.stan_teraz = nastepny_stan

    def Uruchom(self):
        while not self.CzyStanKoncowy(self.stan_teraz): 
            self.WykonajKrok()
           
        
    
    
  
if __name__ == "__main__":
    alfabet = [0,1,2,3,4, ',', '-', 'X', 'Y']
    symbol_pusty = 'A'
    tasma = ['A',1,0,'-',0,4,'A']
    stan_poczatkowy = 'q0'
    przejscia = [
        ['q0', 'q1']
    ]
    stany = {'q0':[['A','A',1, 'q1']],


            'q1':[
                ['X','X',-1,'q2'],
                ['A','A',-1,'q2'],
                [1,1,1,'q1'],
                [2,2,1,'q1'],
                [3,3,1,'q1'],
                [4,4,1,'q1'],
                [',',',',1,'q1'],
                ['-','-',1,'q1'],
                ['Y','Y', 1,'q1'],
            ],
                
            'q2':[
                ['-','-', 0, 'end']
            ],
            'end':'end'
                }
                
    
    Masz = MaszynaTuringa(tasma, alfabet, symbol_pusty, stany, stan_poczatkowy,przejscia)
    Masz.Uruchom()