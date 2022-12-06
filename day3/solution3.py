def getPriorityOfItem(item):
    priority = ord(item) - ord('a') + 1
    if 1 <= priority <= 26:
        return priority
    return ord(item) - ord('A') + 27


def findSameItem(i1, i2, i3):
    for c1 in i1:
        for c2 in i2:
            for c3 in i3:
                if c1 == c2 == c3:
                    return c1


sum = 0
with open("input3.txt") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        #items1 = l.strip()[0:int(len(l) / 2)]
        #items2 = l.strip()[int(len(l) / 2):]
        i1 = lines[i]
        i2 = lines[i+1]
        i3 = lines[i+2]
        sameItem = findSameItem(i1, i2, i3)
        sum += (getPriorityOfItem(sameItem))
print(sum)
