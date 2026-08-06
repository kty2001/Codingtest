# 15652 - N과 M (4)

def dfs(s):
    if len(l) == m: return print(*l)
    for i in range(s, n+1):
        l.append(i)
        dfs(i)
        l.pop()

n, m = map(int, input().split())
l = []
dfs(1)