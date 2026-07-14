def solution(numbers, target):
    def dfs(i, n_i, visited):
        if i == n_i:
            ans = 0
            for i, n in enumerate(numbers):
                ans += n * visited[i]
            return 1 if ans == target else 0
        
        visited.append(-1)
        l = dfs(i+1, n_i, visited)
        visited.pop()
        visited.append(1)
        r = dfs(i+1, n_i, visited)
        visited.pop()
        return l+r
        
    visited = []
    answer = dfs(0, len(numbers), visited)
    return answer