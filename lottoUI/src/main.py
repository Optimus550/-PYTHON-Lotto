import random
import flet as ft

class Lotto:
    def __init__(self, liczby=None, ilosc=None, przedzialy = [range(1, 10), range(10, 20), range(20, 30), range(30, 40), range(40, 50)]):
        if liczby is None:
            self.liczby = []
        else:
            self.liczby = liczby

        if ilosc is None:
            self.ilosc = dict()
        else:
            self.ilosc = ilosc
    
        self.przedzialy = przedzialy

    def buble(self): #sortowanie babelkowe
        n = len(self.liczby)
        for i in range(n-1):
            semafor = False
            for j in range(n-i-1):
                if self.liczby[j]>self.liczby[j+1]:
                    self.liczby[j], self.liczby[j+1] = self.liczby[j+1], self.liczby[j]
                    semafor = True
            if semafor==False:
                break
        return self.liczby

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
        
        self.buble()
        print(f"Wylosowane liczby wg ", end="")
        self.jaki_system(system)
        print(self.liczby)
        print("")
        return self.liczby
    
    def podsumowanie(self): #liczenie z uzyciem slownika
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

class UI: 
    def __init__(self, page: ft.Page):
        self.losy = Lotto() #obiekt klasy Lotto

        self.page = page
        self.page.title='Lotto Losowanie'
        self.page.padding=30
        self.sys_txt=ft.Text(value="System liczbowy")
        self.drpdwn=ft.Dropdown(width=200, value="2-1-1-1-1",
                    options=[
                        ft.DropdownOption(key="2-1-1-1-1", text="2-1-1-1-1"),
                        ft.DropdownOption(key="2-2-2", text="2-2-2"),
                        ft.DropdownOption(key="3-2-1", text="3-2-1"),
                        ft.DropdownOption(key="3-3", text="3-3"),
                        ft.DropdownOption(key="2-2-1-1", text="2-2-1-1"),
                        ft.DropdownOption(key="3-1-1-1", text="3-1-1-1"),
                        ft.DropdownOption(key="4-1-1", text="4-1-1"),
                        ])
        self.los_otp=ft.Text(value="a")
        self.btn_add=ft.Button("Dodaj system", on_click=self.dodaj_system)
        self.okno_wynikow = ft.ListView(
            height=300,          # Sztywna wysokość lub expand=True (zajmie całą resztę okna)
            spacing=2,           # Odstęp między linijkami
            auto_scroll=True,    # MEGA WAŻNE: automatycznie zjeżdża na dół przy nowym tekście
        )
        self.page.add(self.sys_txt, self.drpdwn, self.los_otp, self.btn_add, self.okno_wynikow)

    def dodaj_system(self, e):
        self.drpdwn=ft.Dropdown(width=200, value="2-1-1-1-1",
                    options=[
                        ft.DropdownOption(key="2-1-1-1-1", text="2-1-1-1-1"),
                        ft.DropdownOption(key="2-2-2", text="2-2-2"),
                        ft.DropdownOption(key="3-2-1", text="3-2-1"),
                        ft.DropdownOption(key="3-3", text="3-3"),
                        ft.DropdownOption(key="2-2-1-1", text="2-2-1-1"),
                        ft.DropdownOption(key="3-1-1-1", text="3-1-1-1"),
                        ft.DropdownOption(key="4-1-1", text="4-1-1"),
                        ])
        self.los_otp=ft.Text(value="a")
        self.page.add(self.drpdwn, self.los_otp)

def main(page: ft.Page):
    gui=UI(page)
if __name__ == "__main__":
    ft.run(main)


losowanie = Lotto()

losowanie.losowanko()
losowanie.podsumowanie() #jedna para 2-1-1-1-1

losowanie.losowanko([2, 2, 2])
losowanie.podsumowanie() #2-2-2

losowanie.losowanko([3, 2, 1])
losowanie.podsumowanie() #3-2-1

losowanie.losowanko([3, 3])
losowanie.podsumowanie() #3-3

losowanie.losowanko([2, 2, 1, 1])
losowanie.podsumowanie() #2-2-1-1

losowanie.losowanko([3, 1, 1, 1])
losowanie.podsumowanie() #3-1-1-1

losowanie.losowanko([4, 1, 1])
losowanie.podsumowanie() #4-1-1

losowanie.wyswietl_podsumowanie()