# 19532 - 수학은 비대면강의입니다

a, b, c, d, e, f = map(int, input().split())

if b == 0:
    print(int(c/a), int((f-d*c/a)/e))
elif e == 0:
    print(int(f/d), int((c-a*f/d)/b))
else:
    for x in range(-999, 1000):
            if (c - a*x)/b == (f - d*x)/e:
                print(x, int((c - a*x)/b))
                break