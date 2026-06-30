def solution(dartResult):
    bonus = ['S', 'D', 'T']
    opt = ['*', '#']
    n = []
    b = []
    o = []
    s = ''
    for d in dartResult:
        if d in bonus:
            n.append(int(s))
            s = ''
            b.append(d)
            o.append('')
        elif d in opt:
            o.append(d)
        else: s += d
        
    for i in range(3):
        n[i] = n[i]**(bonus.index(b[i])+1)
        
    for i in range(len(o)):
        idx = o[:i].count('') - 1
        if o[i] == '*':
            if idx == 0:
                n[0] *= 2
            else:
                n[idx], n[idx-1] = n[idx]*2, n[idx-1]*2
        elif o[i] == '#':
            n[idx] *= -1
    return sum(n)