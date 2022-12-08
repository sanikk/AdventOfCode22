def check_down_and_right(taulukko: list, x, y):
    tama = taulukko[y][x]
    nakyy_alhaalta = True
    nakyy_oikealta = True
    for y2 in range(y + 1, len(taulukko)):
        if taulukko[y2][x] >= tama:
            nakyy_alhaalta = False
    for x2 in range(x + 1, len(taulukko[y])):
        if taulukko[y][x2] >= tama:
            nakyy_oikealta = False
    return nakyy_oikealta or nakyy_alhaalta


def main():
    summa = 0
    y_akseli = []
    with open("input.txt") as tiedosto:
        for rivi in tiedosto:
            y_akseli.append([int(x) for x in rivi.strip()])

    longest_from_the_top = [x for x in y_akseli[0]]
    #longest_from_the_top = [9 for x in y_akseli[0]]
    summa += 2 * len(y_akseli[0])
    summa += 2 * len(y_akseli) - 4
    for y in range(1, len(y_akseli) - 1):
        # for y in range(1, 3):
        longest_from_the_left = y_akseli[y][0]
        for x in range(1, len(y_akseli[y]) - 1):
            tama = y_akseli[y][x]
            #print(f"handling ({y},{x}) = {tama} ", end="")
            if tama > longest_from_the_left:
                if tama > longest_from_the_top[x]:
                    longest_from_the_top[x] = tama
                longest_from_the_left = tama
                summa += 1
                #print(f"Näkyy ainakin vasemmalta, {summa=}")
                continue
            #print(f"pisin kun {x=}: {longest_from_the_top[x]=}")
            if tama > longest_from_the_top[x]:
                longest_from_the_top[x] = tama
                summa += 1
                #print(f"Näkyy ainakin ylhäältä, {summa=}")
                continue
            if check_down_and_right(y_akseli, x, y):
                summa += 1
                #print(f"Näkyy oikealta tai alhaalta, {summa=}")
            else:
                pass
                #print(f"Ei näy, {summa=}")
    print(f"{summa=}")


main()
# 9054 too high
# 1617 too high
