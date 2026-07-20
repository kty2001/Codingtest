def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i, com in enumerate(computers):
        for j, c in enumerate(com):
            if c == 1 and i != j:
                graph[i].append(j)
    print(*graph, sep='\n')
    
    answer = 0
    visited = [i for i in range(n)]
    q = []
    while visited:
        q.append(visited.pop())
        answer += 1
        while q:
            cur = q.pop(0)
            for x in graph[cur]:
                if x in visited:
                    visited.remove(x)
                    q.append(x)
    return answer