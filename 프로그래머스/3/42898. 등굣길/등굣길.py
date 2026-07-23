def solution(m, n, puddles):
    answer = 0
    graph = [[1] * m for _ in range(n)]
    for x, y in puddles:
        graph[y-1][x-1] = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    graph[i][j] = graph[i][j-1]
                elif j == 0:
                    graph[i][j] = graph[i-1][j]
                else:
                    graph[i][j] = graph[i][j-1] + graph[i-1][j]

    return graph[n-1][m-1] % 1000000007