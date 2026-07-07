def solution(id_list, report, k):
    answer = []
    stop = []
    
    id_dic = {i: [] for i in id_list}
    yee_dic = {i: 0 for i in id_list}
        
    for r in set(report):
        sin, yee = r.split()
        id_dic[sin].append(yee)
        yee_dic[yee] += 1
        
    for key, value in yee_dic.items():
        if value >= k:
            stop.append(key)
            
    for i in id_list:
        answer.append(len(set(id_dic[i])&set(stop)))
                
    return answer