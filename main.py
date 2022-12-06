def etsi_duplikaatti(jaettava: str):
    puolivali = len(jaettava) // 2
    eka = jaettava[0:puolivali]
    toka = jaettava[puolivali:]
    for merkki in toka:
        if merkki not in eka:
            continue
        return merkki


def muunna_merkki(merkki: str):
    if merkki.islower():
        return ord(merkki) - 96
    return ord(merkki) - 38


summa = 0
with open("input.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()
        #print(f"{rivi = }")
        osuma = etsi_duplikaatti(rivi)
        #print(f"{osuma = }")
        summa += muunna_merkki(osuma)
print(summa)
