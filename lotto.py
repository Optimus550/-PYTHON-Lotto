import random

def buble(lista):
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

def losowanie(pula):
    liczby = []
    losy = list(pula)
    for i in range(0,6):
        losowanie = random.randint(0, 48-i)
        liczby.append(losy[losowanie])
        losy.remove(losy[losowanie])
    buble(liczby)
    print(f"Wylosowane liczby:")
    print(liczby)
    print("")

def losowanie_parami(przedzialy):
    liczby = []
    
    zakres = random.sample(przedzialy, 3)

    for i in zakres:
        zestaw = random.sample(list(i), 2)
        liczby.extend(zestaw)
    
    #pierwotna wersja
    """cyfry = list(pula)
    j=0
    for i in range(0,6,2):
        zakres = random.randint(0, (4-i))
        if przedzialy[zakres]==0:
            indeks = random.randint(0,8-i)
            indeks2 = random.randint(0,8-i-1)
            while indeks2==indeks:
                indeks2 = random.randint(0,8-i-1)
        elif przedzialy[zakres]==1:
            indeks = random.randint(9-i,18-i)
            indeks2 = random.randint(9-i-1,18-i-1)
            while indeks2==indeks:
                indeks2 = random.randint(9-i-1,18-i-1)
        elif przedzialy[zakres]==2:
            indeks = random.randint(19-i,28-i)
            indeks2 = random.randint(19-i-1,28-i-1)
            while indeks2==indeks:
                indeks2 = random.randint(19-i-1,28-i-1)
        elif przedzialy[zakres]==3:
            indeks = random.randint(29-i,38-i)
            indeks2 = random.randint(29-i-1,38-i-1)
            while indeks2==indeks:
                indeks2 = random.randint(29-i-1,38-i-1)
        elif przedzialy[zakres]==4:
            indeks = random.randint(39-i,48-i)
            indeks2 = random.randint(39-i-1,48-i-1)
            while indeks2==indeks:
                indeks2 = random.randint(39-i-1,48-i-1)

        liczby.append(cyfry[indeks])
        liczby.append(cyfry[indeks2])
        j = j + 1
        przedzialy.remove(przedzialy[zakres])
        cyfry.remove(cyfry[indeks])
        cyfry.remove(cyfry[indeks2])
"""
    buble(liczby)
    print(f"Wylosowane liczby parami:")
    print(liczby)
    print("")

def tdi(przedzialy): #trojka dwojka inna
    liczby = []
    
    zakres = random.sample(przedzialy, 3)

    liczby.extend(random.sample(list(zakres[0]), 3))
    liczby.extend(random.sample(list(zakres[1]), 2))
    liczby.extend(random.sample(list(zakres[2]), 1))

    buble(liczby)
    print("Wylosowane liczby 3-2-1:")
    print(liczby)
    print("")

def trzy_trzy(przedzialy):
    liczby = []
    
    zakres = random.sample(przedzialy, 2)

    liczby.extend(random.sample(list(zakres[0]),3))
    liczby.extend(random.sample(list(zakres[1]),3))

    buble(liczby)
    print("Wylosowane liczby 3:3")
    print(liczby)
    print("")


def ttONE(przedzialy):
    liczby = []
    
    zakres = random.sample(przedzialy, 4)

    liczby.extend(random.sample(list(zakres[0]), 2))
    liczby.extend(random.sample(list(zakres[1]), 2))
    liczby.extend(random.sample(list(zakres[2]), 1))
    liczby.extend(random.sample(list(zakres[3]), 1))

    buble(liczby)
    print("Wylosowane liczby 2-2-1-1")
    print(liczby)
    print("")

def threeooo(przedzialy):
    liczby = []
    
    zakres = random.sample(przedzialy, 4)

    liczby.extend(random.sample(list(zakres[0]), 3))
    liczby.extend(random.sample(list(zakres[1]), 1))
    liczby.extend(random.sample(list(zakres[2]), 1))
    liczby.extend(random.sample(list(zakres[3]), 1))

    buble(liczby)
    print("Wylosowane liczby 3-1-1-1")
    print(liczby)
    print("")

def kareta(przedzialy):
    liczby = []
    
    zakres = random.sample(przedzialy, 3)

    liczby.extend(random.sample(list(zakres[0]), 4))
    liczby.extend(random.sample(list(zakres[1]), 1))
    liczby.extend(random.sample(list(zakres[2]), 1))

    buble(liczby)
    print("Wylosowane liczby 4-1-1")
    print(liczby)
    print("")


pula =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
przedzialy = [range(1, 10),
        range(10, 20),
        range(20, 30),
        range(30, 40),
        range(40, 50)]

losowanie(pula) #jedna para 2-1-1-1-1
losowanie_parami(przedzialy) #2-2-2
tdi(przedzialy) #3-2-1
trzy_trzy(przedzialy) #3-3
ttONE(przedzialy)#2-2-1-1
threeooo(przedzialy)#3-1-1-1
kareta(przedzialy)#4-1-1
