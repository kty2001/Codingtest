# 1157 - 단어 공부

word = input().upper()
alpha = {}
for w in word:
    if w not in alpha.keys():
        alpha[w] = word.count(w)
        
tmp = [k for k,v in alpha.items() if max(alpha.values()) == v]
print(*tmp) if len(tmp) == 1 else print("?")