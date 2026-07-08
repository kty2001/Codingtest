def solution(s):
    answer = True
    stack = []
    for a in s:
        if a == '(':
            stack.append(1)
        elif stack and a == ')':
            stack.pop()
        else:
            return False
    if stack: return False

    return True