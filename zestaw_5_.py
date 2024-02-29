def szukaj(nazwaPlikWe, nazwaPlikWy, slowo):
    we=open(nazwaPlikWe,'r')
    lines = we.readlines()
    we.close()
    wy=open(nazwaPlikWy,'w')
    for nr_lini in range(len(lines)):
        line = lines[nr_lini]
        if slowo in line:
            wy.write(f"{nr_lini+1}: {line}")
    wy.close()
    print(f'Wyniki zapisano do pliku: {nazwaPlikWy}')

nazwaPlikWe = 'a.txt'
nazwaPlikWy = 'b.txt'
szukane_slowo = 'egzamin'
#szukaj(nazwaPlikWe, nazwaPlikWy, szukane_slowo)

import re
def znajdz_adresy_email(sciezka_pliku):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    adresy_email = []
    plik = open(sciezka_pliku, 'r')
    lines = plik.readlines()
    for linia in lines:
        wynik=re.findall(pattern,linia)
        if wynik:
            adresy_email.append(wynik)
    return adresy_email
tekst='a.txt'
#adresy = znajdz_adresy_email(tekst)
#print(f'Znalezione adresy e-mail: {adresy}')


def sumujIZapisz(nazwaPliku):
    suma = 0
    try:
        with open(nazwaPliku, 'r') as plik:
            lines = plik.readlines()

        for line in lines:
            if line.strip().isdigit():
                suma += int(line)

        with open(nazwaPliku, 'a') as plik:
            plik.write('\n' + str(suma + 1) + '\n')

    except FileNotFoundError:
        with open(nazwaPliku, 'w') as plik:
            plik.write('1\n')


#sumujIZapisz('a.txt')



def szyfruj(nazwaWe, przesun):

    plik_wejsciowy = open(nazwaWe, 'r')
    tekst = plik_wejsciowy.read()
    plik_wejsciowy.close()

    szyfrowany_tekst = ''
    for znak in tekst:
        if znak.isalpha():
            if znak.islower():
                szyfrowany_tekst += chr((ord(znak) - ord('a') + przesun) % 26 + ord('a'))
            else:
                szyfrowany_tekst += chr((ord(znak) - ord('A') + przesun) % 26 + ord('A'))
        else:
            szyfrowany_tekst += znak
    plik_wyjsciowy = open(f'_{nazwaWe}', 'w')
    plik_wyjsciowy.write(szyfrowany_tekst)
    plik_wyjsciowy.close()

def deszyfruj(nazwaWe, przesun):
    plik_wejsciowy = open(nazwaWe, 'r')
    tekst = plik_wejsciowy.read()
    plik_wejsciowy.close()
    deszyfrowany_tekst = ''
    for znak in tekst:
        if znak.isalpha():
            if znak.islower():
                deszyfrowany_tekst += chr((ord(znak) - ord('a') - przesun) % 26 + ord('a'))
            else:
                deszyfrowany_tekst += chr((ord(znak) - ord('A') - przesun) % 26 + ord('A'))
        else:
            deszyfrowany_tekst += znak

    plik_wyjsciowy = open(f'{nazwaWe}_', 'w')
    plik_wyjsciowy.write(deszyfrowany_tekst)
    plik_wyjsciowy.close()

#szyfruj('a.txt', 4)
#deszyfruj('_a.txt', 4)

def emerytura(nazwaPliku):

    plik_wejsciowy = open(nazwaPliku, 'r')
    lines = plik_wejsciowy.readlines()
    plik_wejsciowy.close()

    emerytura_kobiety = []
    emerytura_mezczyzni = []

    for line in lines:
        imie, nazwisko, plec, wiek = line.strip().split()
        if plec == 'K':
            lata_do_emerytury = 60
        else:
            lata_do_emerytury = 65

        lata_do_emerytury -= int(wiek)

        wynik = f'{nazwisko} {imie} {lata_do_emerytury}\n'

        if plec == 'K':
            emerytura_kobiety.append(wynik)
        else:
            emerytura_mezczyzni.append(wynik)

    plik_kobiety = open('kobiety.txt', 'w')
    plik_kobiety.writelines(emerytura_kobiety)
    plik_kobiety.close()

    plik_mezczyzni = open('mezczyzni.txt', 'w')
    plik_mezczyzni.writelines(emerytura_mezczyzni)
    plik_mezczyzni.close()


#emerytura('b.txt')

def wykres_czestosci(nazwaPliku):
    try:
        plik = open(nazwaPliku, 'r')
        tekst = plik.read().lower()

        czestosci = {}

        for znak in tekst:
            if znak.isalpha():
                czestosci[znak] = czestosci.get(znak, 0) + 1

        najczestszy_znak, liczba_wystapien = max(czestosci.items(), key=lambda x: x[1])

        for znak, ilosc in czestosci.items():
            dlugosc_slupka = int(50 * ilosc / liczba_wystapien)
            print(f"{znak} {'*' * dlugosc_slupka} {ilosc}")

    except FileNotFoundError:
        print(f'Plik {nazwaPliku} nie istnieje.')

    finally:
        plik.close()


#wykres_czestosci('b.txt')


import os


def suma_liczb(katalog):
    suma = 0

    for plik in os.listdir(katalog):
        sciezka = os.path.join(katalog, plik)
        if os.path.isfile(sciezka):
            with open(sciezka, 'r') as file:
                fragmenty = []
                aktualny_fragment = ''
                for znak in file.read():
                    if znak.isdigit() or znak in ('.', '-'):
                        aktualny_fragment += znak
                    elif aktualny_fragment:
                        fragmenty.append(aktualny_fragment)
                        aktualny_fragment = ''

                if aktualny_fragment:
                    fragmenty.append(aktualny_fragment)

                liczby = [float(x) for x in fragmenty]
                suma += sum(liczby)

    print(f'suma: {suma}')

#suma_liczb("katalog_testowy")

def zlicz_wystapienia(sciezka, fraza):
    with open(sciezka, 'r') as plik:
        tresc = plik.read()
        wystapienia = tresc.count(fraza)
    return wystapienia

def znajdz_pliki_z_fraza(katalog, fraza):
    for plik in os.listdir(katalog):
        sciezka = os.path.join(katalog, plik)
        if os.path.isfile(sciezka):
            wystapienia = zlicz_wystapienia(sciezka, fraza)
            if wystapienia > 0:
                print(f'plik: {plik}, wystapienia: {wystapienia}')
            else:
                print(f'plik: {plik}, brak wystąpień')
#znajdz_pliki_z_fraza("katalog_testowy",'ala')
def zamien_tekst(sciezka, stary_tekst, nowy_tekst):
    with open(sciezka, 'r') as file:
        content = file.read()
    with open(sciezka, 'w') as file:
        nowy = content.replace(stary_tekst, nowy_tekst)
        file.write(nowy)

def zamien_tekst_w_katalogu(katalog, stary_tekst, nowy_tekst):
    for plik in os.listdir(katalog):
        sciezka = os.path.join(katalog, plik)
        if os.path.isfile(sciezka):
            zamien_tekst(sciezka, stary_tekst, nowy_tekst)

#zamien_tekst_w_katalogu("katalog_testowy","ala","ALA")



import os

def suma_liczb_calosci_i_zmiennoprzecinkowych(sciezka_do_pliku):
    with open(sciezka_do_pliku, 'r') as plik:
        zawartosc = plik.read()

    calkowite = []
    zmiennoprzecinkowe = []

    for dopasowanie in zawartosc.split():
        if dopasowanie.replace('.', '').replace('-', '').isdigit():
            if '.' in dopasowanie:
                zmiennoprzecinkowe.append(float(dopasowanie))
            else:
                calkowite.append(int(dopasowanie))

    return sum(calkowite), sum(zmiennoprzecinkowe)


def oblicz_stosunek(katalog):
    suma_calkowitych = 0
    suma_zmiennoprzecinkowych = 0

    for nazwa_pliku in os.listdir(katalog):
        sciezka_do_pliku = os.path.join(katalog, nazwa_pliku)
        if os.path.isfile(sciezka_do_pliku):
            suma_calkowitych_pliku, suma_zmiennoprzecinkowych_pliku = suma_liczb_calosci_i_zmiennoprzecinkowych(
                sciezka_do_pliku)
            suma_calkowitych += suma_calkowitych_pliku
            suma_zmiennoprzecinkowych += suma_zmiennoprzecinkowych_pliku

    stosunek = suma_calkowitych / suma_zmiennoprzecinkowych if suma_zmiennoprzecinkowych != 0 else "Nieokreślony (dzielenie przez zero)"
    print(f"Stosunek sumy liczb całkowitych do sumy liczb rzeczywistych: {stosunek}")


#oblicz_stosunek("katalog_testowy")
