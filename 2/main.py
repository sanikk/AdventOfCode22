score = 0
with open("input.txt") as tiedosto:
    for rivi in tiedosto:
        rivi = rivi.strip()
        if rivi == "":
            continue
        osat = rivi.split()
        eka = 0
        toka = 0
        # 1 - rock , 2 - paper , 3 - scissors
        if osat[0] == "A":
            eka = 1
        if osat[0] == "B":
            eka = 2
        if osat[0] == "C":
            eka = 3
        if osat[1] == "X":
            # toka = 1
            # need to lose
            if eka == 1:
                score += 3
            else:
                score += eka - 1
            continue
        if osat[1] == "Y":
            # toka = 2
            # need to draw
            score += 3 + eka
            continue
        if osat[1] == "Z":
            # toka = 3
            # need to win
            if eka == 3:
                score += 6 + 1
            else:
                score += 6 + eka + 1
            continue
        # if eka == toka + 1 or (eka == 1 and toka == 3):
        #    # vastustaja voitti
        #    score += toka
        #    continue
        # if toka == eka + 1 or (eka == 3 and toka == 1):
        #    score += 6 + toka
        #    continue
        # if eka == toka:
        #    score += 3 + toka
print(score)
