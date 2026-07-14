def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    visited = [0, 0] + [0] * (n-1)
    route = [-1, 0] + [20001] * (n-1)
    stack = [1]
    while stack:
        s = stack.pop(0)
        if visited[s] == 1:
            continue
        else:
            visited[s] = 1
            stack += graph[s]
            for g in graph[s]:
                route[g] = min(route[g], route[s] + 1)
    return route.count(max(route))