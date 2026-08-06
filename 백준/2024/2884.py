# 2884 - 알람 시계

h, m = map(int, input().split())
if m < 45:
    h = 23 if h == 0 else h - 1
    m += 15
else:
    m -= 45
print(h, m)