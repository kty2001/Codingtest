# 9012 - 괄호

n = int(input())
for _ in range(n):
    s = []
    a = input()
    for i in a:
        if i == '(': s.append(i)
        elif len(s) > 0: s.pop()
        else:
            print("NO")
            break
    else:
        if len(s) > 0: print("NO")
        else: print("YES")