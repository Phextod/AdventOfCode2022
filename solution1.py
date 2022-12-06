calories = []
top3calories = [0]*3
with open("input1.txt") as f:
    elfSum = 0
    for l in f.readlines():
        if l == '\n':
            calories.append(elfSum)
            elfSum = 0
        else:
            elfSum += int(l)

for c in calories:
    if min(top3calories) < c:
        top3calories[top3calories.index(min(top3calories))] = c

print(sum(top3calories))
