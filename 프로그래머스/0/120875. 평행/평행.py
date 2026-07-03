def solution(dots):
    angle = []
    com = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
    for c in com:
        if (dots[c[0]][1]-dots[c[1]][1]) / (dots[c[0]][0]-dots[c[1]][0]) == (dots[c[2]][1]-dots[c[3]][1]) / (dots[c[2]][0]-dots[c[3]][0]):
            return 1
    return 0