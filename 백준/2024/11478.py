# 11478 - 서로 다른 부분 문자열의 개수

s = input()
c = 0
for i in range(1, len(s) + 1):
    d = {}
    for k in range(len(s) - i + 1):
        a = s[k:k+i]
        if a not in d:
            d[a] = 0
    c += len(d)
print(c)

#-------------------------

st = input()
count = 0
for i in range(1, len(st) + 1):
    some_set = set()
    for k in range(len(st) - i + 1):
        a = st[k:k+i]
        if a not in some_set:
            some_set.add(a)
    count += len(some_set)

print(count)
