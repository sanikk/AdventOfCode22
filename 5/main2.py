def handle_varasto(varasto):
    pinot = []
    vika = varasto.pop().strip()
    montako = int(vika.split()[-1])
    for i in range(montako):
        pinot.append([])
    # sitten täytetään noi pinot
    for i in range(len(varasto) - 1, -1, -1):
        rivi = varasto[i]
        #print(f"{rivi = }")
        # osumat indekseissä 1, 5, 9
        for i in range(1, len(rivi), 4):
            if rivi[i] != " ":
                pinot[(i-1)//4].append(rivi[i])

#    print("PRINTING PINOT BEFORE RETURNING")
#    for pino in pinot:
#        print(pino)
    return pinot


def main():
    pinot = []
    kehikko = True
    varasto = []
    #round = 1
    with open("input.txt") as tiedosto:
        for rivi in tiedosto:
            if kehikko:
                # eli noi pinot ensin
                varasto.append(rivi)
                if rivi.startswith(" 1"):
                    pinot = handle_varasto(varasto)
                    kehikko = False
            else:
                if rivi.strip() == "":
                    continue
                osat = rivi.split()
                montako = int(osat[1])
                mista = int(osat[3]) - 1
                mihin = int(osat[5]) - 1
                # pinot[mihin].extend(pinot[mista][0:montako])
                pinot[mihin].extend(pinot[mista][-montako:])
                del pinot[mista][-montako:]
                #print(f"ROUND {round}:")
                # for pino in pinot:
                #    print(pino)
                #round += 1
    for pino in pinot:
        print(pino.pop(), end="")
    print("")


main()
