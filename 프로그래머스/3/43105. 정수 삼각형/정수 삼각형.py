def solution(triangle):
    answer = 0
    for i, tri in enumerate(triangle):
        if i == 0: continue
        for j, t in enumerate(tri):
            if j == 0:
                tri[j] += triangle[i-1][0]
            elif j == i:
                tri[j] += triangle[i-1][j-1]
            else:
                tri[j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])