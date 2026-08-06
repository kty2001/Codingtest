# 4134 - 다음 소수

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
        continue
    while True:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: break
        else:
            print(n)
            break
        n += 1

#-------------------------------

import sys
input = sys.stdin.readline
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
testcase = int(input())
for i in range(testcase):
    n = int(input())
    while not is_prime(n):
        n += 1
    print(n)