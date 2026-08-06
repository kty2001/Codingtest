# 5622 - 다이얼

arr = input()
t = 0
for s in arr:
    if s in "ABC":
        t += 3
    elif s in "DEF":
        t += 4
    elif s in "GHI":
        t += 5
    elif s in "JKL":
        t += 6
    elif s in "MNO":
        t += 7
    elif s in "PQRS":
        t += 8
    elif s in "TUV":
        t += 9
    elif s in "WXYZ":
        t += 10
print(t)