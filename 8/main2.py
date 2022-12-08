def main():
    paras_score = 0
    taulukko = []
    with open("input.txt") as tiedosto:
        for rivi in tiedosto:
            taulukko.append([int(x) for x in rivi.strip()])

    for y in range(1, len(taulukko) - 1):
        for x in range(1, len(taulukko[y]) - 1):
            tama = taulukko[y][x]

            laskuri = 0
            for x2 in range(x - 1, -1, -1):
                laskuri += 1
                if taulukko[y][x2] >= tama:
                    break
            if laskuri == 0:  # score is 0 anyway
                continue
            score = laskuri
            laskuri = 0
            for x2 in range(x+1, len(taulukko[y])):
                laskuri += 1
                if taulukko[y][x2] >= tama:
                    break
            if laskuri == 0:  # score is 0 anyway
                continue
            score *= laskuri
            laskuri = 0
            for y2 in range(y - 1, -1, -1):
                laskuri += 1
                if taulukko[y2][x] >= tama:
                    break
            if laskuri == 0:  # score is 0 anyway
                continue
            score *= laskuri
            laskuri = 0
            for y2 in range(y + 1, len(taulukko)):
                laskuri += 1
                if taulukko[y2][x] >= tama:
                    break
            if laskuri == 0:
                continue
            score *= laskuri
            #print(f"({x},{y}) = {tama}, {score=}")
            if score > paras_score:
                paras_score = score
    print(f"{paras_score=}")


main()
# 9054 too high
# 1617 too high
