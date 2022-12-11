signal = ""
with open("input6.txt") as f:
    signal = f.readline()

currentSignal = signal[:14]
for i, c in enumerate(signal):
    if i < 14:
        continue
    badSignal = False
    for testC in currentSignal:
        if currentSignal.count(testC) > 1:
            badSignal = True
            break
    if not badSignal:
        print(i)
        break
    currentSignal = currentSignal[1:]
    currentSignal += c
