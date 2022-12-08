def main():
    storage = []
    needed_size = 9199225
    with open("input.txt") as tiedosto:
        for rivi in tiedosto:
            storage.append(rivi.strip())
        if storage[0] == "$ cd /":
            dirname = "/"
        if storage[1] == "$ ls":
            #koko, laskuri, summa = filecrawler2(storage, "/", 2, 0)
            koko, laskuri, summa, lista = filecrawler(
                storage, "/", 2, 0, [], needed_size)
            if koko < 100000:
                summa += koko
            print(f"root: {koko = }")
            if koko > needed_size:
                lista.append((koko, "/"))
            lista.sort()
            for hakemisto in lista:
                print(hakemisto)
            print(f"used space = {koko}")
            unused_space = 70000000 - koko
            needed_size = 30000000 - unused_space
            print(f"unused space = {unused_space}")
            print(f"needed space = {needed_size}")
            # 9199225


def filecrawler(data: list, dirname: str, laskuri: int, summa: int, lista, needed_size: int):
    koko = 0
    while laskuri < len(data):
        rivi = data[laskuri]
        laskuri += 1
        if rivi.startswith("$"):
            osat = rivi.split()
            if osat[1] == "cd":
                if osat[2] == "..":
                    # print(f"{dirname=}, {koko=}, {koko > needed_size}")
                    if koko < 100000:
                        summa += koko
                    if koko > needed_size:
                        print(f"appending {koko=}, {dirname=}")
                        lista.append((koko, dirname))
                    return koko, laskuri, summa, lista
                else:
                    lisa_koko, rivi, summa, lista = filecrawler(
                        data, osat[2], laskuri, summa, lista, needed_size=needed_size)
                    koko += lisa_koko
                    laskuri = rivi
        else:
            osat = rivi.split()
            if osat[0] != "dir":
                koko += int(osat[0])
    if dirname != "/":
        if koko > needed_size:
            lista.append((koko, dirname))
    return koko, laskuri, summa, lista


main()
