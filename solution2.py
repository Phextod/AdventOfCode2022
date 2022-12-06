def outcomeScore(oInt, mInt):
    score = mInt + 1
    if oInt == mInt:
        score += 3
    elif oInt == (mInt + 1) % 3:
        score += 0
    else:
        score += 6
    return score


def pickToInt(pick):
    mInt = ord(pick) - ord('X')
    if 2 >= mInt >= 0:
        return mInt
    return ord(pick) - ord('A')


def stratToInt(outcome):
    return {
        "X": -1,
        "Y": 0,
        "Z": 1
    }[outcome]


def scoreByStrat(opponent, strat):
    oInt = pickToInt(opponent)
    sInt = stratToInt(strat)
    mInt = (oInt + sInt) % 3
    return outcomeScore(oInt, mInt)


scores = []
with open("input2.txt") as f:
    for l in f.readlines():
        s = l.strip().split(' ')
        #scores.append(outcomeScore(pickToInt(s[0]), pickToInt(s[1])))
        scores.append(scoreByStrat(s[0], s[1]))

print(sum(scores))
