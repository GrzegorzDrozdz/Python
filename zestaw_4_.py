def Zadanie1():
    ciag = input("Podaj ciąg znaków: ")
    ostatni_char = ciag[-1]
    licznik = 0
    for i in ciag:
        if i == ostatni_char:
            licznik += 1
    print(f"W słowie {ciag} występuje {licznik} razy litera {ostatni_char}")

# Zadanie1()

def Zadanie1_B():
    ciag = input("Podaj ciąg znaków: ")
    ostatni_char = ciag[-1]
    licznik = ciag.count(ostatni_char)
    print(f"W słowie {ciag} występuje {licznik} razy litera {ostatni_char}")

# Zadanie1_B()


def Zadanie2(palindrom):
    lista_znakow = [znak.lower() for znak in palindrom if znak.isalnum()]
    print(lista_znakow)
    bol = True
    for i in range(len(lista_znakow)):
        j = len(lista_znakow) - 1 - i
        if lista_znakow[i] != lista_znakow[j]:
            bol = False
            break
    print(bol)

#Zadanie2("zakopane na pokaz")
#Zadanie2("Ala ma kota")


def Zadanie3(tekst):
    suma=0
    for char in tekst:
        if char.isdigit():
            suma+=int(char)
    return suma
#print(Zadanie3('Ala ma 1 psa i 2 koty. Jola ma 10 rybek i 2 papugi.'))


def Szyfr_Cezara():
    string=input("Podaj łańcuch znaków do zaszyfrowania: ")
    liczba=int(input("Podaj przesunięcie:"))
    nowy = ""
    for element in string:
        kodascii = ord(element)
        po_przesunieciu = kodascii + liczba
        if po_przesunieciu > ord('z'):
            po_przesunieciu -= 26
            char = chr(po_przesunieciu)
            nowy += char
        elif po_przesunieciu < ord('a'):
            po_przesunieciu += 26
            char = chr(po_przesunieciu)
            nowy += char
        else:
            char = chr(po_przesunieciu)
            nowy += char
    print(nowy)
#Szyfr_Cezara()


import re
def strToInt(s):

    match = re.match(r'[-+]?\d+', s)

    if match:

        result = int(match.group())
    else:

        result = 0

    return result


print(strToInt("-13krowa"))
print(strToInt("+12"))
print(strToInt("0001"))
print(strToInt("991-234-23"))
print(strToInt("+zonk"))
print(strToInt(""))
print(strToInt("-12e5"))
print(strToInt("-12e-5"))

def czyAnagram(t1, t2):
    t1 = t1.replace(" ", "").replace(".","").replace(",","").lower()
    t2 = t2.replace(" ", "").replace(".","").replace(".","").lower()
    t1_list = list(t1)
    t2_list = list(t2)
    t1_list.sort(key=str.lower)
    t2_list.sort(key=str.lower)
    return t1_list==t2_list

"""print(czyAnagram("kolej", "olejk"))
print(czyAnagram("kolej", "kole"))
print(czyAnagram("kolej", "K O L E J"))
print(czyAnagram("Gregory House", "Huge ego, sorry"))"""


def HTMLColor2RGB(color):
    red = color[1:3]
    green = color[3:5]
    blue = color[5:7]

    r = int(red, 16)
    g = int(green, 16)
    b = int(blue, 16)

    return [r, g, b]



print(HTMLColor2RGB("#FF0050"))
print(HTMLColor2RGB("#001020"))
