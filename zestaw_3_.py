import random

def Zadanie1():
    lista1 = []
    lista2 = []
    n = int(input("podaj wielkosc listy1: "))
    m = int(input("podaj wielkosc listy2: "))

    for i in range(n):
        lista1.append(random.randint(1, 10))
    for j in range(m):
        lista2.append(random.randint(1, 10))
    print(f"lista 1 : {lista1}")
    print(f"lista 2 : {lista2}")
    zbior1 = set(lista1)
    zbior2 = set(lista2)
    iloczyn_zbiorow = zbior1 & zbior2
    print(iloczyn_zbiorow)
#Zadanie1()

def Zadanie2():
    zdanie = input("wpisz zdanie: ")
    lista = zdanie.split()
    slownik = {}
    for element in lista:
        slownik[element] = slownik.get(element, 0) + 1
    print(slownik)
    zbior_unikalny = set(lista)
    print(zbior_unikalny)
#Zadanie2()

def Zadanie4_zlicz_znaki(string):
    dict = {}
    for char in string:
        dict[char] = dict.get(char, 0) + 1
    return dict
#print(Zadanie4_zlicz_znaki("Za Zasługi dla Finansów Publicznych Rzeczypospolitej Polskiej"))

def liczba_na_slowa(liczba):
    if liczba < 0 or liczba >= 1000000:
        return "Liczba spoza zakresu (0-999999)"

    jednosci = {0: 'zero', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery', 5: 'pięć', 6: 'sześć', 7: 'siedem', 8: 'osiem', 9: 'dziewięć'}
    nastki = {10: 'dziesięć', 11: 'jedenaście', 12: 'dwanaście', 13: 'trzynaście', 14: 'czternaście', 15: 'piętnaście', 16: 'szesnaście', 17: 'siedemnaście', 18: 'osiemnaście', 19: 'dziewiętnaście'}
    dziesiatki = {2: 'dwadzieścia', 3: 'trzydzieści', 4: 'czterdzieści', 5: 'pięćdziesiąt', 6: 'sześćdziesiąt', 7: 'siedemdziesiąt', 8: 'osiemdziesiąt', 9: 'dziewięćdziesiąt'}
    setki = {1: 'sto', 2: 'dwieście', 3: 'trzysta', 4: 'czterysta', 5: 'pięćset', 6: 'sześćset', 7: 'siedemset', 8: 'osiemset', 9: 'dziewięćset'}

    def przeksztalc_liczbe(liczba):
        if liczba < 10:
            return jednosci[liczba]
        elif liczba < 20:
            return nastki[liczba]
        elif liczba < 100:
            dziesiatka = liczba // 10
            reszta = liczba % 10
            return dziesiatki[dziesiatka] + ('' if reszta == 0 else ' ' + jednosci[reszta])
        elif liczba < 1000:
            setka = liczba // 100
            reszta = liczba % 100
            return setki[setka] + ('' if reszta == 0 else ' ' + przeksztalc_liczbe(reszta))

    tysiecy = liczba // 1000
    reszta = liczba % 1000

    wynik = ''
    if tysiecy == 1:
        wynik += przeksztalc_liczbe(tysiecy) + ' tysiąc '
    elif 1<tysiecy<5:
        wynik += przeksztalc_liczbe(tysiecy) + ' tysiące '
    elif tysiecy>5:
        wynik += przeksztalc_liczbe(tysiecy) + ' tysięcy '
    if reszta > 0:
        wynik += przeksztalc_liczbe(reszta)

    return wynik
#print(liczba_na_slowa(2115))
#print(liczba_na_slowa(987654))

def zadanie6_fiszki():
    print("Program do tworzenia fiszek.")
    print("Jeśli chcesz zakończyć dodawanie fiszek, wpisz 'Q'.")
    fiszki = {}
    while True:
        slowo = input("Podaj słowo: ")
        if slowo.lower() == 'q':
            break
        znaczenie = input("Podaj znaczenie: ")
        fiszki[slowo] = znaczenie
    poprawne = 0
    bledne = 0
    while fiszki:
        slowo = random.choice(list(fiszki.keys()))
        znaczenie = fiszki[slowo]
        print(f"Co to znaczy: {slowo}?")
        odpowiedz = input("Twoja odpowiedź: ")
        if odpowiedz.lower() == 'q':
            break
        if odpowiedz == znaczenie:
            print("Poprawna odpowiedź!")
            poprawne += 1
        else:
            print(f"Nieprawidłowa odpowiedź. Prawidłowe znaczenie to: {znaczenie}")
            bledne += 1
        del fiszki[slowo]

    print(f"Koniec fiszek. Poprawne odpowiedzi: {poprawne}, Błędne odpowiedzi: {bledne}")
#zadanie6_fiszki()






