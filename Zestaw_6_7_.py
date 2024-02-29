import math

class Wektor:
    def __init__(self, x=0, y=0):
        self._x = float(x)
        self._y = float(y)

    def dlugosc(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def normalizuj(self):
        dlugosc = self.dlugosc()
        if dlugosc != 0:
            return Wektor(self._x / dlugosc, self._y / dlugosc)
        else:
            return Wektor()

    def wyswietl(self):
        return f"Wektor [{self._x}, {self._y}] o długości {self.dlugosc()}"

    def __add__(self, w):
        return Wektor(self._x + w._x, self._y + w._y)

    def __sub__(self, w):
        return Wektor(self._x - w._x, self._y - w._y)



    def __iadd__(self, w):
        self._x += w._x
        self._y += w._y
        return self

    def __isub__(self, w):
        self._x -= w._x
        self._y -= w._y
        return self

    def __str__(self):
        return f"[{self._x}, {self._y}]"

    def __mul__(self, a):
        return Wektor(self._x * a, self._y * a)

    def __rmul__(self, a):
        return Wektor(a *self._x , a * self._y )


"""w1 = Wektor(2,4)
w2 = Wektor(1.5)
print("Wektor w1:", w1, "wektor w2:", w2)
print("Dł. w1 =", w1.dlugosc(), "dł. w2 =", w2.dlugosc())
print("w1+w2 =", w1+w2)
print("w1-w2 =", w1-w2)
print("w1*2 =", w1*2)
print("-3*w2 =", -3*w2)
print("w1*2-w2 =", w1*2-w2)
print("w1 po normalizacji =", w1.normalizuj())
print("w2 po normalizacji =", w2.normalizuj())
print(w1.wyswietl())
print(w2.wyswietl())"""

class ElementZamowienia:
    def __init__(self, nazwa, cena, ilosc):
        self._nazwa = nazwa
        self._cena = cena
        self._ilosc = ilosc
        self._rabat = 0

    def obliczKoszt(self):
        return self._cena * self._ilosc

    def obliczRabat(self):
        koszt = self.obliczKoszt()
        if self._ilosc >= 5:
            self._rabat = koszt * 0.1
        else:
            self._rabat = 0
        return self._rabat

    def obliczonyKoszt(self):
        return self.obliczKoszt() - self._rabat

    def __str__(self):
        return f"{self._nazwa} {self._cena:.2f} zł, {self._ilosc} szt., łącznie {self.obliczKoszt():.2f} zł"


class Zamowienie:
    def __init__(self, maksRozmiar):
        self._elementy = []
        self._rozmiar = 0
        self._maksRozmiar = maksRozmiar

    def dodaj(self, elZam):
        if self._rozmiar < self._maksRozmiar:
            self._elementy.append(elZam)
            self._rozmiar += 1
            return True
        else:
            return False

    def obliczKoszt(self):
        koszt_calkowity = sum(elZam.obliczonyKoszt() for elZam in self._elementy)
        return koszt_calkowity

    def pisz(self):
        print("Zamówienie:")
        for el in self._elementy:
            rabat = el.obliczRabat()
            print(el)
            print(f"Naliczony rabat: {rabat:.2f} zł")
        calkowity_koszt = self.obliczKoszt()
        print(f"Łączny koszt zamówienia: {calkowity_koszt}")


z = Zamowienie(10)
z.dodaj(ElementZamowienia("Chleb", 4.0, 2))
z.dodaj(ElementZamowienia("Mleko", 2.5, 1))
z.dodaj(ElementZamowienia("Cukier", 4.0, 5))
z.dodaj(ElementZamowienia("Puszka", 9.0, 1))
z.pisz()


