def solution(numbers):
    from itertools import permutations as per
    answer = 0
    n = set()
    for i in range(1, len(numbers)+1):
        num = list(per(numbers, i))
        for nu in num:
            n.add(int(''.join(nu)))
    
    for i in n:
        if i == 0 or i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer