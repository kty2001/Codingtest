def solution(bandage, health, attacks):
    answer = 0
    cur = health
    cnt = 1
    for i in range(1, attacks[-1][0] + 1):
        # 공격 판단 여부
        if i == attacks[0][0]:
            cur -= attacks[0][1]
            cnt = 1
            if cur <= 0:
                return -1
            attacks.pop(0)
        
        else:
            if cnt == bandage[0]:
                cur = min(health, cur + bandage[1] + bandage[2])
                cnt = 0
            else:
                cur = min(health, cur + bandage[1])
            cnt += 1
        print(f'time:{i} / cur:{cur} / cnt:{cnt}')
    return cur