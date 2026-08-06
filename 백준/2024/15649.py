# 15649 - N과 M (1)

def dfs():
    if len(l) == m: return print(*l)
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        l.append(i)
        dfs()
        l.pop()
        visited[i] = False

n, m = map(int, input().split())
l = []
visited = [False] * (n+1)
dfs()