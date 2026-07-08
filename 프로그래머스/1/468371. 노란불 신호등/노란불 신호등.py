def solution(signals):
    import math
    sig = ['G'*s[0] + 'Y'*s[1] + 'R'*s[2] for s in signals]
    i_max = math.lcm(*(sum(s) for s in signals))
    
    for i in range(i_max):
        if all(s[i%len(s)] == 'Y' for s in sig): return i + 1
    return -1