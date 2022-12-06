def oneContainTheOther(elf1, elf2):
    e1 = list(map(int, elf1.split("-")))
    e2 = list(map(int, elf2.split("-")))
    """if (e1[0] <= e2[0]) and (e2[1] <= e1[1]):
        return True
    elif (e2[0] <= e1[0]) and (e1[1] <= e2[1]):
        return True"""
    if (e1[1] < e2[0]) or (e2[1] < e1[0]):
        return False
    return True


with open("input4.txt") as f:
    lines = f.readlines()
    count = 0
    for l in lines:
        elves = l.strip().split(",")
        if oneContainTheOther(elves[0], elves[1]):
            count += 1

print(count)
