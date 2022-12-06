def etsi_latka(lista: list):
    osumat = set()
    for merkki in lista[0]:
        if merkki in lista[1] and merkki in lista[2]:
            return merkki


kolmikko = []
summa = 0
with open('input.txt') as tiedosto:
    for rivi in tiedosto:
        kolmikko.append(rivi)
        if len(kolmikko) == 3:

            tulos = etsi_latka(kolmikko)
            if tulos.islower():
                summa += ord(tulos) - 96
            else:
                summa += ord(tulos) - 38
            kolmikko = []
            # do something here with tulos
print(summa)
