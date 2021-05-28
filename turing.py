import numpy as np
from abc import *
#lubie plaski

class GrafAbstrakcyjny(ABC):

     # Właciwość zwracająca macierz połączeń grafu. 
    @abstractproperty
    def Polaczenia(self):
        pass
    
    # Właściwość zwracająca macierz wag połączeń między węzłami grafu.
    @abstractproperty
    def Wagi(self):
        pass

    # Właściwość zwracająca listę węzłów grafu.
    @abstractproperty
    def Wezly(self):
        pass

    # Właściwość mówiąca o tym, czy graf jest skierowany
    @abstractproperty
    def Skierowany(self):
        pass

class graf(GrafAbstrakcyjny):
    def __init__(self, A, B, C):#A - lista węzłów, B - m.połączeń, C- m.wag
        if B.shape != C.shape or B.shape[0] != B.shape[1] or C.shape[0] != C.shape[1] or len(A)  != B.shape[0]:
            raise Exception("Nie spełnia warunków")     
        self.wezly = A[:]
        self.polaczenia = np.array(B)
        self.wagi = np.array(C)
    def skierowany(self): 
        if (np.transpose(self.polaczenia) == self.polaczenia).sum() == self.polaczenia.shape[0] * self.polaczenia.shape[1]:
            return True
        else:
            return False
    def wypisz(self):
        print("Lista węzłów:\n", self.wezly)
        print("Macierz połączeń:\n", self.polaczenia)
        print("Macierz wag:\n", self.wagi)

    @property
    def Wezly(self):
        return self.wezly
    @property
    def Polaczenia(self):
        return self.polaczenia
    @property
    def Wagi(self):
        return self.wagi
    @property
    def Skierowany(self):
        if (np.transpose(self.polaczenia) == self.polaczenia).sum() == self.polaczenia.shape[0] * self.polaczenia.shape[1]:
            return True
        else:
            return False
# class Graf(GrafAbstrakcyjny):
#     # @property
#     # def skierowany(self):
#     #     super().skierowany()
#     #     # lub
#     #     GrafAbstrakcyjny.skierowany(self)
    
#     @property
#     def Wezly(self):
#         return self.Wez
#     @property
#     def Polaczenia(self):
#         return self.P
#     @property
#     def Wagi(self):
#         return self.Wag
#     @property
#     def Skierowany(self):
#         if (np.transpose(self.P) == self.P).sum() == self.P.shape[0] * self.P.shape[1]:
#             return True
#         else:
#             return False

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
    