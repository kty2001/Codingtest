def solution(park, routes):
    answer = []
    h, w = len(park), len(park[0])
    for i, p in enumerate(park):
        if 'S' in p:
            pos = [i, p.index('S')]

    for r in routes:
        o, t = r.split()
        t = int(t)
        
        if o == 'E':
            for i in range(1, t+1):
                if pos[1]+i >= w or park[pos[0]][pos[1]+i] == 'X':
                    break
            else:
                pos[1] += t
        elif o == 'W':
            for i in range(1, t+1):
                if pos[1]-i < 0 or park[pos[0]][pos[1]-i] == 'X':
                    break
            else:
                pos[1] -= t
        elif o == 'N':
            for i in range(1, t+1):
                if pos[0]-i < 0 or park[pos[0]-i][pos[1]] == 'X':
                    break
            else:
                pos[0] -= t
        elif o == 'S':
            for i in range(1, t+1):
                if pos[0]+i >= h or park[pos[0]+i][pos[1]] == 'X':
                    break
            else:
                pos[0] += t
    return pos