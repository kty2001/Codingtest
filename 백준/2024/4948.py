# 4948 - 베르트랑 공준

import sys
a = [1 for _ in range(246912+1)]
a[0], a[1] = 0, 0
for i in range(2, int(246912**0.5)+1):
    if a[i] == 1:
        for j in range(2, 246912//i + 1):
            a[i*j] = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    print(sum(a[n+1:n*2+1]))