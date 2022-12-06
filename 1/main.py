biggest = 0
calory_list = []
with open("input.txt") as tiedosto:
    calories_now = 0
    for rivi in tiedosto:
        rivi = rivi.strip()
        if rivi == "":
            if calories_now > biggest:
                biggest = calories_now
            calory_list.append(calories_now)
            calories_now = 0
            continue
        calories_now += int(rivi)
    if calories_now > biggest:
        biggest = calories_now
    if calories_now > 0:
        calory_list.append(calories_now)
print(biggest)
calory_list.sort()
print(calory_list)
print(calory_list[-1]+calory_list[-2]+calory_list[-3])
