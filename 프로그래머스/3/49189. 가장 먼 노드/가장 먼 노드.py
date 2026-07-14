def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    route = [-1] * (n+1)
    route[1] = 0
    
    stack = [1]
    while stack:
        s = stack.pop(0)
        
        for g in graph[s]:
            if route[g] == -1:
                route[g] = route[s] + 1
                stack.append(g)
    return route.count(max(route))