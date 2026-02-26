import random

def buble(lista): #sortowanie babelkowe
    semafor = False
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                semafor = True
        if semafor==False:
            break
    return lista

def jaki_system(system):
    for i in range(len(system)):
        print(system[i], end="")
        if i==len(system)-1:
            print("")
        else:
            print("-", end="")
        

def losowanko(przedzialy, system=[2,1,1,1,1]): #losowanie
    liczby = []
    n = len(system)
    zakres = random.sample(przedzialy, n)

    for i in range(n):
        liczby.extend(random.sample(list(zakres[i]), system[i]))
    
    buble(liczby)
    print(f"Wylosowane liczby wg ", end="")
    jaki_system(system)
    print(liczby)
    print("")
    return liczby

def podsumowanie(ilosc, liczby): #liczenie z uzyciem slownika
    for i in liczby:
        ilosc[i] = ilosc.get(i, 0) + 1
    return ilosc

def wyswietl_podsumowanie(ilosc):
    posortowany = dict(sorted(ilosc.items(), key=lambda item: item[1], reverse=True))
    print(f"\n========Wystąpienia liczb========")
    k = "raz(y)."
    for i in posortowany:
        print(f"Liczba {i:>2} wystąpiła: {str(posortowany[i]):>1} {k:>8}")
    print(f"==================================")
przedzialy = [range(1, 10),
        range(10, 20),
        range(20, 30),
        range(30, 40),
        range(40, 50)]

ilosc = dict()

podsumowanie(ilosc,losowanko(przedzialy)) #jedna para 2-1-1-1-1
podsumowanie(ilosc,losowanko(przedzialy, [2, 2, 2])) #2-2-2
podsumowanie(ilosc,losowanko(przedzialy, [3, 2, 1])) #3-2-1
podsumowanie(ilosc,losowanko(przedzialy, [3, 3])) #3-3
podsumowanie(ilosc,losowanko(przedzialy, [2, 2, 1, 1])) #2-2-1-1
podsumowanie(ilosc,losowanko(przedzialy, [3, 1, 1, 1])) #3-1-1-1
podsumowanie(ilosc,losowanko(przedzialy, [4, 1, 1])) #4-1-1
wyswietl_podsumowanie(ilosc)
#losowanko(przedzialy, [5, 1]) #5-1
#losowanko(przedzialy, [6]) #6 identycznych