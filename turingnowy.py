import numpy as np
from abc import *
import logging

class AbstrackMaszynaTuringa(ABC):   
    @abstractproperty
    def ListaStanow(self):
        pass
    @abstractproperty
    def Przejscia(self):
        pass

    @abstractmethod
    def __init__(self, alfabet, symbol_pusty, stany, stan_początkowy, przejscia):
        pass
    @abstractmethod
    def WykonajKrok(self, ZnakZTasmy):
        pass
    @abstractmethod
    def Uruchom(self, Tasma):
        pass
    @abstractmethod
    def CzyStanPoczątkowy(self, stan):
        pass
    @abstractmethod
    def CzyStanKoncowy(self, stan):
        pass
    
    
class MaszynaTuringa(AbstrackMaszynaTuringa):
    def __init__(self, alfabet, stany, stan_poczatkowy):
        self.alfabet = alfabet 
        self.stany = stany
        self.stan_poczatkowy = stan_poczatkowy
        self.head = 0
        self.stan_teraz = self.stan_poczatkowy
    def ListaStanow(self):
        return self.stany.keys() 
    def Przejscia(self):
        return self.stany
    def CzyStanPoczątkowy(self, stan):
        return stan == self.stan_poczatkowy
    def CzyStanKoncowy(self, stan):
        return stan == 'end'
    #dajindex - zwraca na którym miejscu w poszczególnym stanie(liście) stany['q1'][^tu^] stoi dany znak | ^tu^- nie chcemy znaku tylko int indexu
    def DajIndex(self, stany, wCzymSzukamy, czegoSzukamy):
        i = 0 
        #print('w czym szukamy --', self.stany[wCzymSzukamy])
        for i in range(len(self.stany[wCzymSzukamy])):
            #print('pierwsza w danym stanie --',self.stany[wCzymSzukamy][i][0], '|||||  czegoSzukamy --', czegoSzukamy)
            if self.stany[wCzymSzukamy][i][0] == czegoSzukamy:
                return i

    def WykonajKrok(self, ZnakZTasmy):
        stan_obecny = self.stan_teraz #w jakim stanie teraz jestem 

        #Zwraca następny stan 
        a = self.DajIndex(self.stany, stan_obecny, ZnakZTasmy)
        nastepny_stan = self.stany[stan_obecny][a][3]

        #zamienia znak na tasmie i zmienia head, czyli położenie głowicy
        self.tasma[self.head] = self.stany[stan_obecny][a][1]
        self.head += self.stany[stan_obecny][a][2]
        #podmienia stan
        self.stan_teraz = nastepny_stan

    def Uruchom(self, Tasma):
        
        self.tasma = Tasma
        print(self.tasma,'\t', self.head)
        while 1: 
            if( self.CzyStanKoncowy(self.stan_teraz)):
                break

            self.WykonajKrok(Tasma[self.head])
            print(self.tasma,'\t', self.head)
            
           
        
    
    
  
if __name__ == "__main__":
    alfabet = [0,1,2,3,4, ',', '-', 'X', 'Y', 'A']
    tasma = ['A',1,1,'Y','-', 0,4,'A']
    stan_poczatkowy = 'q0'
    stany = {'q0':[['A','A',1, 'q1']],


            'q1':[
                ['X','X',-1,'q2'], 
                ['A','A',-1,'q2'], 
                [0,0,1,'q1'],
                [1,1,1,'q1'],
                [2,2,1,'q1'],
                [3,3,1,'q1'],
                [4,4,1,'q1'],
                [',',',',1,'q1'],
                ['-','-',1,'q1'],
                ['Y','Y', 1,'q1'],
            ],
                
            'q2':[
                ['-','-', 0, 'end'],
                [0,'X',-1, 'q_0'], #jaki stan
                [1,'X',-1,'q_1'],
                [2,'X',-1,'q_2'],
                [3,'X',-1,'q_3'],
                [4,'X',-1,'q_4'],
            ],

             'q_0': [
                 ['-', '-', -1, 'q_0'],
                 [0, 0, -1, 'q_0'],  # jaki stan
                 [1, 1, -1, 'q_0'],
                 [2, 2, -1, 'q_0'],
                 [3, 3, -1, 'q_0'],
                 [4, 4, -1, 'q_0'],
                 ['Y', 'Y', -1, 'q_0_'],
             ],

             'q_1': [
                 ['-', '-', -1, 'q_1'],
                 [0, 0, -1, 'q_1'],  # jaki stan
                 [1, 1, -1, 'q_1'],
                 [2, 2, -1, 'q_1'],
                 [3, 3, -1, 'q_1'],
                 [4, 4, -1, 'q_1'],
                 ['Y', 'Y', -1, 'q_1_'],
             ],

             'q_2': [
                 ['-', '-', -1, 'q_2'],
                 [0, 0, -1, 'q_2'],  # jaki stan
                 [1, 1, -1, 'q_2'],
                 [2, 2, -1, 'q_2'],
                 [3, 3, -1, 'q_2'],
                 [4, 4, -1, 'q_2'],
                 ['Y', 'Y', -1, 'q_2_'],
             ],

             'q_3': [
                 ['-', '-', -1, 'q_3'],
                 [0, 0, -1, 'q_3'],  # jaki stan
                 [1, 1, -1, 'q_3'],
                 [2, 2, -1, 'q_3'],
                 [3, 3, -1, 'q_3'],
                 [4, 4, -1, 'q_3'],
                 ['Y', 'Y', -1, 'q_3_'],
             ],

             'q_4': [
                 ['-', '-', -1, 'q_4'],
                 [0, 0, -1, 'q_4'],  # jaki stan
                 [1, 1, -1, 'q_4'],
                 [2, 2, -1, 'q_4'],
                 [3, 3, -1, 'q_4'],
                 [4, 4, -1, 'q_4'],
                 ['Y', 'Y', -1, 'q_4_'],
             ],

             'q_0_': [
                 [0, 'Y', 1, 'q_0_0'],  # jaki stan
                 [1, 'Y', 1, 'q_0_1'],
                 [2, 'Y', 1, 'q_0_2'],
                 [3, 'Y', 1, 'q_0_3'],
                 [4, 'Y', 1, 'q_0_4'],
             ],

             'q_1_': [
                 [0, 'Y', 1, 'q_1_0'],  # jaki stan
                 [1, 'Y', 1, 'q_1_1'],
                 [2, 'Y', 1, 'q_1_2'],
                 [3, 'Y', 1, 'q_1_3'],
                 [4, 'Y', 1, 'q_1_4'],
             ],

             'q_2_': [
                 [0, 'Y', 1, 'q_2_0'],  # jaki stan
                 [1, 'Y', 1, 'q_2_1'],
                 [2, 'Y', 1, 'q_2_2'],
                 [3, 'Y', 1, 'q_2_3'],
                 [4, 'Y', 1, 'q_2_4'],
             ],

             'q_3_': [
                 [0, 'Y', 1, 'q_3_0'],  # jaki stan
                 [1, 'Y', 1, 'q_3_1'],
                 [2, 'Y', 1, 'q_3_2'],
                 [3, 'Y', 1, 'q_3_3'],
                 [4, 'Y', 1, 'q_3_4'],
             ],

             'q_4_': [
                 [0, 'Y', 1, 'q_4_0'],  # jaki stan
                 [1, 'Y', 1, 'q_4_1'],
                 [2, 'Y', 1, 'q_4_2'],
                 [3, 'Y', 1, 'q_4_3'],
                 [4, 'Y', 1, 'q_4_4'],
             ],

             'q_0_0': [
                 ['Y', 0, -1, 'Q1'],  # jaki stan
             ],

             'q_0_1': [
                 ['Y', 1, -1, 'Q1'],  # jaki stan
             ],

             'q_0_2': [
                 ['Y', 2, -1, 'Q1'],  # jaki stan
             ],

             'q_0_3': [
                 ['Y', 3, -1, 'Q1'],  # jaki stan
             ],

             'q_0_4': [
                 ['Y', 4, -1, 'Q1'],  # jaki stan
             ],

             'q_1_0': [
                 ['Y', 4, -1, 'Q2'],  # jaki stan
             ],

             'q_1_1': [
                 ['Y', 0, -1, 'Q1'],  # jaki stan
             ],

             'q_1_2': [
                 ['Y', 1, -1, 'Q1'],  # jaki stan
             ],

             'q_1_3': [
                 ['Y', 2, -1, 'Q1'],  # jaki stan
             ],

             'q_1_4': [
                 ['Y', 3, -1, 'Q1'],  # jaki stan
             ],

             'q_2_0': [
                 ['Y', 3, -1, 'Q2'],  # jaki stan
             ],

             'q_2_1': [
                 ['Y', 4, -1, 'Q2'],  # jaki stan
             ],

             'q_2_2': [
                 ['Y', 0, -1, 'Q1'],  # jaki stan
             ],

             'q_2_3': [
                 ['Y', 1, -1, 'Q1'],  # jaki stan
             ],

             'q_2_4': [
                 ['Y', 2, -1, 'Q1'],  # jaki stan
             ],

             'q_3_0': [
                 ['Y', 2, -1, 'Q2'],  # jaki stan
             ],

             'q_3_1': [
                 ['Y', 3, -1, 'Q2'],  # jaki stan
             ],

             'q_3_2': [
                 ['Y', 4, -1, 'Q2'],  # jaki stan
             ],

             'q_3_3': [
                 ['Y', 0, -1, 'Q1'],  # jaki stan
             ],

             'q_3_4': [
                 ['Y', 1, -1, 'Q1'],  # jaki stan
             ],

             'q_4_0': [
                 ['Y', 1, -1, 'Q2'],  # jaki stan
             ],

             'q_4_1': [
                 ['Y', 2, -1, 'Q2'],  # jaki stan
             ],

             'q_4_2': [
                 ['Y', 3, -1, 'Q2'],  # jaki stan
             ],

             'q_4_3': [
                 ['Y', 4, -1, 'Q2'],  # jaki stan
             ],

             'q_4_4': [
                 ['Y', 0, -1, 'Q1'],  # jaki stan
             ],

             'Q1': [
                 [0, 0, -1, 'Q1'],  # jaki stan
                 [1, 1, -1, 'Q1'],
                 [2, 2, -1, 'Q1'],
                 [3, 3, -1, 'Q1'],
                 [4, 4, -1, 'Q1'],
                 ['Y', 'Y', -1, 'Q1'],
                 ['A', 'A', 1, 'q1'],
             ],

             'Q2': [
                 ['Y', 'Y', -1, 'Q3'],
             ],

             'Q3': [
                 [0, 4, -1, 'Q3'],  # jaki stan
                 [1, 0, -1, 'Q1'],
                 [2, 1, -1, 'Q1'],
                 [3, 2, -1, 'Q1'],
                 [4, 3, -1, 'Q1'],
             ],


            'end':'end',
            
                }
                
    
    Masz = MaszynaTuringa(alfabet, stany, stan_poczatkowy)
    Masz.Uruchom(tasma)
    