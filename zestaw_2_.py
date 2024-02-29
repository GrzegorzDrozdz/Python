import random
def Zadanie1():
    l = [random.randint(-10, 10) for _ in range(10)]
    print(l)
    print(f"wartość maksymalna: {max(l)}, wartość minimalna: {min(l)}")
    #samemu min i max
    max_wartosc = l[0]
    for element in l:
        if element > max_wartosc:
            max_wartosc = element
    min_wartosc = l[0]
    for element in l:
        if element < min_wartosc:
            min_wartosc = element
    print(f"max wartosc {max_wartosc}, min wartosc {min_wartosc}")
    #srednia
    suma = 0
    licznik=0
    for element in l:
        suma+=element
        licznik+=1
    srednia = suma/licznik
    print(f"średnia arytmetyczna elementów listy: {srednia}")
 #ile elementów jest > lub < od średniej
    licznikWiekszych = 0
    for element in l:
        if (element > srednia):
            licznikWiekszych += 1
    print(f"liczba elementów tablicy wiekszych od średniej: {licznikWiekszych}")
    LicznikMniejszych = 0
    for element in l:
        if (element < srednia):
            LicznikMniejszych += 1
    print(f"liczba elementów tablicy mniejszych od średniej: {LicznikMniejszych}")
    #wyświetlenie listy w odwrotnej kolejnosci
    print(l[::-1])
#Zadanie1()

def Zadanie2():
    l = [random.randint(1, 10) for _ in range(20)]
    print(l)
    for i in range(1,11):
        licznik=0
        for element in l:
           if i==element:
               licznik+=1
        print(f"{i} - {licznik}")
#Zadanie2()

def Zadanie3():
    macierz = [[random.randint(-5, 5) for _ in range(5)]for _ in range(5)]
    #wyświetlenie
    for wiersz in macierz:
        for x in wiersz:
            print(f"{x:3.0f}", end="")
        print()


    kolumny = [[] for _ in range(5)]

    # dodaje do listy wartości w kolumach
    for wiersz in macierz:
        for i in range(5):
            kolumny[i].append(wiersz[i])

    maxy=[]
    miny=[]
    for i in range(5):
        maxy.append(max(kolumny[i]))
        miny.append(min(kolumny[i]))
    print(f"tablica najmiejszych wartosci z kolumny {miny}")
    print(f"tablica najwiekszych wartosci z kolumny {maxy}")
#Zadanie3()

def Zadanie4():
    import math
    lista = []
    a = int(input("podaj liczę dodatnią a: "))
    b = int(input("podaj liczę dodatnią b: "))

    if a>b:
        temp = b
        b = a
        a = temp
    for i in range(a,b+1):
        if i%2!=0:
            lista.append(i)
    print(lista)
    #teraz tworze krotki
    krotki = [(x, 2 ** x, math.sqrt(x)) for x in lista]
    print("Lista krotek:", krotki)
#Zadanie4()

def Zadanie5():
    a = int(input("podaj minimalną wartość: "))
    b = int(input("podaj maksymalną wartość: "))
    n = int(input("podaj wymiar macierzy: "))
    macierz = [[random.randint(a, b) for _ in range(n)] for _ in range(n)]
    for wiersz in macierz:
        for x in wiersz:
            print(f"{x:4.0f}", end="")
        print()

    SumaPrzekatna1 = 0
    SumaPrzekatna2 = 0
    for i in range(n):
        SumaPrzekatna1+=macierz[i][i]
    print(f"suma przekątnej: {SumaPrzekatna1}")

    for i in range(n):
        SumaPrzekatna2+=macierz[i][n-i-1]
    print(f"suma przekątnej: {SumaPrzekatna2}")

    SumaNieparzystych = 0
    for i in range(1,n):
        for j in range(n):
            if i%2 == 1 and j%2==1:
                SumaNieparzystych += macierz[i][j]
    print(f"suma elementów na nieparzystych indeksach: {SumaNieparzystych}")
"""
    odwrocona_macierz=macierz
    for wiersz in odwrocona_macierz:
        wiersz.reverse()
    odwrocona_macierz.reverse()

    for wiersz in odwrocona_macierz:
        for x in wiersz:
            print(f"{x:4.0f}", end="")
        print()
"""
#Zadanie5()

def Zadanie6():
    n = int(input("Podaj liczbę (> 0): "))
    macierz = [['' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            liczbai = i + 1
            liczbaj = j + 1
            dzielniki_i = [x for x in range(1, 1 + liczbai) if liczbai % x == 0]
            dzielniki_j = [x for x in range(1, 1 + liczbaj) if liczbaj % x == 0]
            wspolne_dzielniki = []
            for dzielnik in dzielniki_j:
                if dzielnik in dzielniki_i:
                    wspolne_dzielniki.append(dzielnik)
            if len(wspolne_dzielniki) == 1:
                macierz[i][j] = '+'
            else:
                macierz[i][j] = '.'

    for i in range(n):
        for j in range(n):
            print(macierz[i][j], end=" ")
        print()
#Zadanie6()
