def solution(today, terms, privacies):
    answer = []
    for i, pri in enumerate(privacies):
        d, t = pri.split()
        for term in terms:
            if t in term:
                l = int(term.split()[1])
        y_diff = int(today.split('.')[0]) - int(d.split('.')[0])
        m_diff = int(today.split('.')[1]) - int(d.split('.')[1])
        d_diff = int(today.split('.')[2]) - int(d.split('.')[2])
        if y_diff*12*28 + m_diff*28 + d_diff >= l*28:
            answer.append(i+1)
    return answer