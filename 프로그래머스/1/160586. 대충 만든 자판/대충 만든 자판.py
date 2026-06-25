def solution(keymap, targets):
    answer = []
    al = {chr(i+65): 1e5 for i in range(26)}
    for k in keymap:
        for i in range(len(k)):
            al[k[i]] = min(al[k[i]], i+1)
    for target in targets:
        ans = sum(al[t] for t in target)
        if ans < 1e5: answer.append(ans)
        else: answer.append(-1)
    return answer