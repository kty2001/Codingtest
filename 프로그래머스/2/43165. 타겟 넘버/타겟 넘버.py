def solution(numbers, target):
    def dfs(i, n_i, visited):
        if i == n_i:
            ans = 0
            for i, n in enumerate(numbers):
                ans += n * visited[i]
            if ans == target:
                answer[0] += 1
            return True
        
        visited.append(-1)
        dfs(i+1, n_i, visited)
        visited.pop()
        visited.append(1)
        dfs(i+1, n_i, visited)
        visited.pop()
        
    
    visited = []
    answer = [0]
    dfs(0, len(numbers), visited)
    return answer[0]