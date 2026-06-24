def solution(lottos, win_nums):
    cnt = sum(1 for l in lottos if l in win_nums)
    return [min(7 - cnt - lottos.count(0), 6), min(7 - cnt, 6)]