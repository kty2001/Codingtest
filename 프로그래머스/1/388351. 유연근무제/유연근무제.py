def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i, s in enumerate(schedules):
        for j, t in enumerate(timelogs[i]):
            if (j + startday) % 7 == 0 or (j + startday) % 7 == 6:
                continue
            s_h, s_m = s//100, s%100 + 10
            t_h, t_m = t//100, t%100
            if (s_h - t_h)*60 + (s_m - t_m) < 0:
                break
        else:
            answer += 1    
    return answer