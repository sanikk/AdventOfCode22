def main():
    muisti = []
    tulos = 0
    with open("input.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.strip()
            for merkki in rivi:
                tulos += 1
                if len(muisti) == 14:
                    muisti.pop(0)
                if len(muisti) == 13 and merkki not in muisti:
                    if tarkista(muisti):
                        return tulos
                muisti.append(merkki)


def tarkista(lista):
    for merkki in lista:
        if lista.count(merkki) != 1:
            return False
    return True


print(main())
