def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    y = [0, 0, 1, -1]
    x = [1, -1, 0, 0]
    
    # BFS
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    q = [[0, 0]]
    while q:
        i, j = q.pop(0)
        for k in range(4):
            dy, dx = y[k], x[k]
            if 0 <= i+dy < n and 0 <= j+dx < m:
                if not visited[i+dy][j+dx] and maps[i+dy][j+dx] > 0:
                    visited[i+dy][j+dx] = True
                    q.append([i+dy, j+dx])
                    maps[i+dy][j+dx] = maps[i][j] + 1
    
    if visited[n-1][m-1] == False: return -1
    return maps[n-1][m-1]