# 4949 - 균형잡힌 세상

import sys
input = sys.stdin.readline
while True:
    a = input().rstrip()
    if a == '.': break
    s = []
    for i in a:
        if i == '(': s.append(i)
        elif i == '[': s.append(i)
        elif i == ')':
            if len(s) > 0 and s[-1] == "(":
                s.pop()
            else:
                print('no')
                break
        elif i == ']':
            if len(s) > 0 and s[-1] == "[":
                s.ㅈpop()
            else:
                print('no')
                break
    else: 
        if len(s) == 0: print('yes')
        else: print('no')