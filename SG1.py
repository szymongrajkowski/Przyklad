class person:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        
lista = []
while True:
    imie = str(input("Podaj imie"))
    nazwisko = str(input("Podaj nazwisko"))
    pesel = (input("Podaj pesel"))

    nowaosoba = person(imie,nazwisko,pesel)
    
    lista.append(nowaosoba)

    for osoba in lista:
        print(osoba.imie,osoba.nazwisko,osoba.pesel)
