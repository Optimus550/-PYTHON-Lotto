import random

class Lotto:
    def __init__(self, liczby=None, ilosc=None, lista=None, przedzialy = [range(1, 10), range(10, 20), range(20, 30), range(30, 40), range(40, 50)]):
        if liczby is None:
            self.liczby = []
        else:
            self.liczby = liczby

        if ilosc is None:
            self.ilosc = dict()
        else:
            self.ilosc = ilosc

        if lista is None:
            self.lista = []
        else:
            self.lista = lista
    
        self.przedzialy = przedzialy

    def buble(self, lista): #sortowanie babelkowe
        semafor = False
        n = len(self.lista)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.lista[j]>self.lista[j+1]:
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
                    semafor = True
            if semafor==False:
                break
        return self.lista

    def jaki_system(self, system):
        for i in range(len(system)):
            print(system[i], end="")
            if i==len(system)-1:
                print("")
            else:
                print("-", end="")
            
    
    def losowanko(self, system=[2,1,1,1,1]): #losowanie
        self.liczby = []
        n = len(system)
        zakres = random.sample(self.przedzialy, n)
    
        for i in range(n):
            self.liczby.extend(random.sample(list(zakres[i]), system[i]))
        
        self.buble(self.liczby)
        print(f"Wylosowane liczby wg ", end="")
        self.jaki_system(system)
        print(self.liczby)
        print("")
        return self.liczby
    
    def podsumowanie(self, liczby): #liczenie z uzyciem slownika
        for i in self.liczby:
            self.ilosc[i] = self.ilosc.get(i, 0) + 1
        return self.ilosc
    
    def wyswietl_podsumowanie(self):
        posortowany = dict(sorted(self.ilosc.items(), key=lambda item: item[1], reverse=True))
        print(f"\n========Wystąpienia liczb========")
        k = "raz(y)."
        for i in posortowany:
            print(f"Liczba {i:>2} wystąpiła: {str(posortowany[i]):>1} {k:>8}")
        print(f"==================================")

losowanie = Lotto()
losowanie.podsumowanie(losowanie.losowanko()) #jedna para 2-1-1-1-1
losowanie.podsumowanie(losowanie.losowanko([2, 2, 2])) #2-2-2
losowanie.podsumowanie(losowanie.losowanko([3, 2, 1])) #3-2-1
losowanie.podsumowanie(losowanie.losowanko([3, 3])) #3-3
losowanie.podsumowanie(losowanie.losowanko([2, 2, 1, 1])) #2-2-1-1
losowanie.podsumowanie(losowanie.losowanko([3, 1, 1, 1])) #3-1-1-1
losowanie.podsumowanie(losowanie.losowanko([4, 1, 1])) #4-1-1
losowanie.wyswietl_podsumowanie()