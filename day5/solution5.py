operation = []
stacks = []
with open("input5.txt") as f:
    lines = f.readlines()
    stackEndIndex = 0
    for l in lines:
        stackEndIndex += 1
        if l == "\n":
            break
        for i in range(len(l)):
            stackIndex = i // 4
            while len(stacks) < stackIndex+1:
                stacks.append([])
            if l[i] == "[":
                crate = l[i + 1]
                stacks[stackIndex].append(crate)
            else:
                i += 4
    for stack in stacks:
        stack.reverse()
    print(stacks)
    for l in lines:
        if stackEndIndex > 0:
            stackEndIndex -= 1
            continue
        s = l.strip().split(" ")
        amount = int(s[1])
        fromStack = int(s[3])-1
        toStack = int(s[5])-1
        #for i in range(amount):
        movedCrates = stacks[fromStack][-amount:]
        del stacks[fromStack][-amount:]
        stacks[toStack] += movedCrates
            #movedBox = stacks[fromStack].pop(-1)
            #stacks[toStack].append(movedBox)
    print("".join([x[-1] for x in stacks]))
