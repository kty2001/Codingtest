def solution(mats, park):
    answer = -1
    for m in sorted(mats, reverse=True):
        for i in range(len(park) - m + 1):
            for j in range(len(park[0]) - m + 1):
                if all('-1' == park[i+x][j+y] for x in range(m) for y in range(m)):
                    return m
    return answer