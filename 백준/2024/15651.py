# 15651 - N과 M (3)

def dfs():
    if len(l) == m: return print(*l)
    for i in range(1, n+1):
        l.append(i)
        dfs()
        l.pop()

n, m = map(int, input().split())
l = []
dfs()