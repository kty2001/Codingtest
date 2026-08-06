# 15650 - N과 M (2)

def dfs(s):
    if len(l) == m: return print(*l)
    for i in range(s, n+1):
        if visited[i] == True: continue
        l.append(i)
        visited[i] = True
        dfs(i+1)
        l.pop()
        visited[i] = False

n, m = map(int, input().split())
l = []
visited = [False] * (n+1)
dfs(1)