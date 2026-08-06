# 1269 - 대칭 차집합

n, m = map(int, input().split())
a = {}
b = {}
for i in list(map(int, input().split())):
    a[i] = 0
for i in list(map(int, input().split())):
    b[i] = 0
c = {}
d = {}
for i in a:
    if i not in b: c[i] = 0
for i in b:
    if i not in a: d[i] = 0
print(len(c)+len(d))

#---------------------------

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(len(a)+len(b) - 2*len(set(a)&set(b)))