# 1436 - 영화감독 숌

n = int(input())
i = 666
while n > 0:
    if '666' in str(i):
        n -= 1
        if n == 0:
            print(i)
            break
    i += 1

#--------------------------------
N = int(input())

from itertools import product

# 모든 조합을 생성
all_cases = [''.join(n) for n in product('0123456789s', repeat=5)]
# s가 포함된 엘리먼트에 한하여 s를 666으로 대체 후 정수로 변환
all_cases = [int(n.replace('s', '666')) for n in all_cases if 's' in n]
# 중복된 엘리먼트 제거
all_cases = list(set(all_cases))

# 오름차순으로 정렬 (총 55722개의 경우의 수)
all_cases.sort()
# 1-베이스
print(all_cases[N-1])