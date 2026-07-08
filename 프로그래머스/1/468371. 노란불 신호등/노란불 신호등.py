def solution(signals):
    answer = -1
    
#     sig = [[s[0], s[1], sum(s)] for s in signals]
#     o, r, l = zip(*sig)
#     om = max(o)
    
#     equal_loop = 0
#     if 1 == len(set(l)):
#         equal_loop = 1
    
#     i = 1
#     while True:
#         if equal_loop and (i > om+l[0]):
#             return -1
#         for s in sig:
#             if (i-s[0]) % s[2] >= s[1]: break
#         else: return i+1
#         i += 1
    
    sig = ['G'*s[0] + 'Y'*s[1] + 'R'*s[2] for s in signals]
    sig_len = [sum(s) for s in signals]
    i_max = 1
    for s in sig_len:
        i_max *= s
    
    i = 0
    while True:
        if i > i_max: return -1
        if {s[i%len(s)] for s in sig} == {'Y'}:
            return i + 1
        i += 1
    
    return answer