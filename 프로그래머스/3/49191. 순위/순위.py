def solution(n, results):
    answer = 0
    graph = [[0]*(n) for _ in range(n)]
    for w, l in results:
        graph[w-1][l-1] = 1
        graph[l-1][w-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue
                elif graph[i][j] == 0:
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                        graph[j][i] = -1
                    elif graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1
                        graph[j][i] = 1
                        
    for g in graph:
        if g.count(0) == 1:
            answer += 1
    return answer