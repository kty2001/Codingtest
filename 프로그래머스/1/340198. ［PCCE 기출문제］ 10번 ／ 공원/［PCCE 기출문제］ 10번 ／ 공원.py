def solution(mats, park):
    answer = -1
    for m in sorted(mats, reverse=True):
        for i in range(len(park) - m + 1):
            for j in range(len(park[0]) - m + 1):
                if park[i][j] == '-1':
                    flag = 1
                    for x in range(m):
                        for y in range(m):
                            if park[i+x][j+y] != '-1':
                                flag = 0
                                break
                        if flag == 0: break
                    else:
                        return m
    
    return answer