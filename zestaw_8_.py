class Samochod:
    def __init__(self, marka="None", zuzyciePaliwa=0):
        self.marka = marka
        self.zuzyciePaliwa = zuzyciePaliwa

    def koszt(self, km, cena):
        return km * self.zuzyciePaliwa/100 * cena

    def wyswietl(self):
        return f"Samochód marki {self.marka}, zużycie paliwa: {self.zuzyciePaliwa} l/100 km"

class Autobus(Samochod):
    def __init__(self, marka="Autobus", zuzyciePaliwa=20, lMiejsc=50):
        super().__init__(marka, zuzyciePaliwa)
        self.lMiejsc = lMiejsc

    def wyswietl(self):
        return f"Autobus marki {self.marka}, zużycie paliwa: {self.zuzyciePaliwa} l/100 km, liczba miejsc: {self.lMiejsc}"

class Ciezarowka(Samochod):
    def __init__(self, marka="Ciezarowka", zuzyciePaliwa=30, nosnosc=5000):
        super().__init__(marka, zuzyciePaliwa)
        self.nosnosc = nosnosc

    def wyswietl(self):
        return f"Ciężarówka marki {self.marka}, zużycie paliwa: {self.zuzyciePaliwa} l/100 km, nośność: {self.nosnosc} kg"


s = Samochod("Toyota", 8)
a = Autobus("Mercedes", 15, 40)
c = Ciezarowka("Volvo", 25, 10000)

print(s.wyswietl())
print("Koszt podróży samochodem:", s.koszt(100, 6), "zł")

print(a.wyswietl())
print("Koszt podróży autobusem:", a.koszt(100, 6), "zł")

print(c.wyswietl())
print("Koszt podróży ciężarówką:", c.koszt(100, 6), "zł")



class Statek:
    def __init__(self, wspolrzedne1, wspolrzedne2):
        self.wspolrzedne1 = wspolrzedne1
        self.wspolrzedne2 = wspolrzedne2
        self.maszty = [True]

    def strzal(self, wsp1, wsp2):
        for i in range(len(self.maszty)):
            if wsp1 == self.wspolrzedne1 and wsp2 == self.wspolrzedne2 + i:
                self.maszty[i] = False
                if all(m == False for m in self.maszty):
                    return 2
                else:
                    return 1

        return 0

    def wyswietl(self):
        print(f"Współrzędne: {self.wspolrzedne1}, {self.wspolrzedne2}")


class Statek2Maszty(Statek):
    def __init__(self, wspolrzedne1, wspolrzedne2):
        super().__init__(wspolrzedne1, wspolrzedne2)
        self.maszty = [True, True]


class Statek3Maszty(Statek):
    def __init__(self, wspolrzedne1, wspolrzedne2):
        super().__init__(wspolrzedne1, wspolrzedne2)
        self.maszty = [True, True, True]


statek1 = Statek(1, 1)
statek2_maszty = Statek2Maszty(2, 2)
statek3_maszty = Statek3Maszty(3, 3)

print("Statek 1:")
statek1.wyswietl()
print("Rezultat strzału:", statek1.strzal(1, 1))
statek1.wyswietl()

print("\nStatek 2 maszty:")
statek2_maszty.wyswietl()
print("Rezultat strzału:", statek2_maszty.strzal(2, 2))
statek2_maszty.wyswietl()
print("Rezultat strzału:", statek2_maszty.strzal(2, 3))
statek2_maszty.wyswietl()

print("\nStatek 3 maszty:")
statek3_maszty.wyswietl()
print("Rezultat strzału:", statek3_maszty.strzal(3, 3))
statek3_maszty.wyswietl()
print("Rezultat strzału:", statek3_maszty.strzal(3, 4))
statek3_maszty.wyswietl()
print("Rezultat strzału:", statek3_maszty.strzal(3, 5))
statek3_maszty.wyswietl()




