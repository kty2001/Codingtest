def solution(ingredient):
    answer = 0
    stack = ''
    ingre = ''.join(map(str, ingredient))
    burger = '1231'
    # while burger in ingre:
    #     ingre = ingre.replace(burger, '', 1)
    for i in ingre:
        stack += i
        if stack[-4:] == burger:
            stack = stack[:-4]
            answer += 1
    # answer = (len(ingredient) - len(ingre)) // 4
    return answer