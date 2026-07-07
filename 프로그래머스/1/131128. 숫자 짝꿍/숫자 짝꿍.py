def solution(X, Y):
    # dig = {str(i): min(X.count(str(i)), Y.count(str(i))) for i in range(10)}
    # print(dig)
    # answer = ''.join(k*v for k, v in dig.items())[::-1]
    # if not answer:
    #     return '-1'
    # print(str(int(answer)))
    
    x_d = {str(i): 0 for i in range(10)}
    y_d = {str(i): 0 for i in range(10)}
    for x in X:
        x_d[x] += 1
    for y in Y:
        y_d[y] += 1
        
    ans = {}
    for i in range(10):
        ans[str(i)] = min(x_d[str(i)], y_d[str(i)])
    print(ans)
    
    answer = ''
    for i in range(9, -1, -1):
        answer += str(i) * ans[str(i)]
    
    if len(answer) == 0:
        return '-1'
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer