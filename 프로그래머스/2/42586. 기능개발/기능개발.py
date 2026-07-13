def solution(progresses, speeds):
    answer = []
    t = [(100-progresses[i]-1)//speeds[i]  + 1 for i in range(len(speeds))]
    s = []
    for i in t:
        if not s:
            s.append(i)
        elif s[0] >= i:
            s.append(i)
        else:
            answer.append(len(s))
            s = [i]
    answer.append(len(s))
    return answer