def Zad1() :
    wzrost=float(input("podaj wzrost w metrach np (1.8): "))
    waga = float(input("podaj wagę w kilogramach: "))
    bmi=waga/wzrost**2
    if(18.5<=bmi<=24.9):
        print(f"waga prawidłowa : {bmi:.2f}")
    elif(bmi<18.5):
        print(f"niedowaga: {bmi:.2f}")
    else:
        print(f"nadwaga: {bmi:.2f}")
#Zad1()

def Zad2():
    while True:
        cena =float(input("podaj cenę towaru: "))
        raty =float(input("podaj ilosc rat: "))

        if 100<=cena<=10000 and 6<=raty<=48:
            print("dane wejściowe są poprawne ")
            if 6 <= raty <= 12:
                oprocentowanie = 0.025
            elif 13 <= raty <= 24:
                oprocentowanie = 0.05
            else:
                oprocentowanie = 0.1

            kwota_kredytu = cena * (1 + oprocentowanie)
            rata_miesieczna = kwota_kredytu / raty

            print(f"Miesięczna rata wynosi: {rata_miesieczna:.2f} zł")
            break
        else :
            print("dane wejściowe są niepoprawne, podaj ponownie: ")
#Zad2()

def Zadanie3():
    liczba = int(input("podaj liczbę całkowitą dodatnią: "))
    for i in range(1,liczba+1):
        if(i%2!=0):
            print(i)
        i+=1
#Zadanie3()

def Zadanie4():
    liczba = int(input("podaj liczbę całkowitą dodatnią: "))
    for i in range(1, liczba + 1):
        if (2**i<=liczba):
            print(2**i)
        i += 1

#Zadanie4()

def Zadanie5():
    suma = 0
    while True:
        liczba = float(input("Podaj liczbę: "))
        if liczba == 0:
            break
        suma += liczba
    print(f"Suma liczb wynosi {suma}")
#Zadanie5()

def Zadanie6():
    suma = 0
    max = 0
    min = 0
    avg = 0
    licznik=0
    while True:
        liczba = int(input("Podaj liczbę: "))
        if liczba == 0:
            break
        elif liczba > max:
            max = liczba
        else:
            min = liczba
        suma += liczba
        licznik += 1
        avg = suma / licznik
    print(f"Suma liczb wynosi {suma}, średnia wynosi: {avg:.2f}, max {max}, min {min}")
#Zadanie6()

def Zadanie7():
    import random
    losowa = random.randint(1,100)
    while True :
        liczba = int(input("zgadnij liczbę z przedziału 1-100 : "))

        if losowa>liczba:
            print("podałeś za małą wartość")
        elif losowa<liczba:
            print("podałeś za dużą wartość")
        else:
            print("gratuluję")
            break
#Zadanie7()

def Zadanie8():
    liczba = float(input("podaj liczbe: "))
    suma = 0
    suma_parzyste = 0
    suma_nieparzyste = 0
    licznik_parzyste=0
    licznik_nieparzyste=0
    while liczba > 0:
        cyfra = liczba % 10
        suma += cyfra
        if cyfra % 2 == 0:
            suma_parzyste += cyfra
            licznik_parzyste += 1
        else:
            suma_nieparzyste += cyfra
            licznik_nieparzyste += 1
        liczba //= 10
    print(f"suma {suma}")
    print(f"suma_parzyste {suma_parzyste}")
    print(f"suma_nieparzyste {suma_nieparzyste}")
    srednia_parzyste=suma_parzyste/licznik_parzyste
    srednia_nieparzyste=suma_nieparzyste/licznik_nieparzyste
    print(f"srednia parzyste {srednia_parzyste}")
    print(f"srednia nieparzyste {srednia_nieparzyste}")
    stosunek_cyfr=srednia_parzyste/srednia_nieparzyste
    print(f"stosunek parzyste:nieparzyste wynosi {stosunek_cyfr}")
#Zadanie8()

def Zadanie9():
    liczba = int(input("podaj liczbe aby wyświetlić jej dzielniki: "))
    for i in range(1,liczba+1):
        if liczba%i==0:
            print(i)
#Zadanie9()


def Zadanie10():
    liczba = int(input("podaj liczbe aby sprawdzić czy jest liczbą pierwszą: "))
    licznik=0

    for i in range(1,liczba+1):
         if liczba%i==0:
            licznik+=1
    if(licznik==2):
        print(f"liczba {liczba} jest liczbą pierwszą")
    else:
        print("nie jest liczbą pierwszą")
#Zadanie10()

