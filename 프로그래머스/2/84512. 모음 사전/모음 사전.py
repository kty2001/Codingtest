def solution(word):
    mo = ['A', 'E', 'I', 'O', 'U']
    dic = []
    
    def dfs(s, l):
        if l > 5: return
    
        dic.append(s)
        for m in mo:
            s += m
            dfs(s, l+1)
            s = s[:-1]
            
    dfs('', 0)
    return dic.index(word)