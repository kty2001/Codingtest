# 12789 - 도키도키 간식드리미

n = int(input())
a = list(map(int, input().split()))
m = max(a)
d = []
c = 1
while c <= m:
    if not a and d[-1] != c:
        print("Sad")
        break
    elif a and a[0] == c:
        c += 1
        a.pop(0)
    elif d and d[-1] == c:
        c += 1
        d.pop()
    else:
        d.append(a[0])
        a.pop(0)
else: print("Nice")