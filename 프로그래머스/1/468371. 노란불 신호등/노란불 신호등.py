def solution(signals):
    sig = ['G'*s[0] + 'Y'*s[1] + 'R'*s[2] for s in signals]
    i_max = 1
    for s in signals:
        i_max *= sum(s)
    
    for i in range(i_max):
        if {s[i%len(s)] for s in sig} == {'Y'}: return i + 1
    return -1