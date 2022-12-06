laskuri = 0
with open("input.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()

        molemmat = rivi.split(",")

        ekan = molemmat[0].split("-")
        ekan = [int(x) for x in ekan]
        tokan = molemmat[1].split("-")
        tokan = [int(x) for x in tokan]

        if ekan[0] <= tokan[0] and ekan[1] >= tokan[0]:
            laskuri += 1
        elif tokan[0] <= ekan[0] and tokan[1] >= ekan[0]:
            laskuri += 1
        elif ekan[0] <= tokan[1] and ekan[1] >= tokan[1]:
            laskuri += 1
        elif tokan[0] <= ekan[1] and tokan[1] >= ekan[1]:
            laskuri += 1

print(laskuri)  # 881
