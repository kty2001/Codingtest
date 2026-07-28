def solution(word):
    mo = ['A', 'E', 'I', 'O', 'U']
    dic = []
    
    def dfs(string, l):
        if l > 5:
            return
        if string not in dic:
            dic.append(string)
        for m in mo:
            string += m
            dfs(string, l+1)
            string = string[:-1]
    for m in mo:
        dfs(m, 1)
    
    dic.sort()
    
    return dic.index(word) + 1