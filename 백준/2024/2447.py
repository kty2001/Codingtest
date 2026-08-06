# 2447 - 별 찍기 - 10

def star(s, n):
    p = n//3
    if p == 0: return s
    f = star(s[:p], p)
    m = s[p:p*2]
    for i in range(p):
        for j in range(len(m[0])):
            if (j // p) % 3 == 1:
                m[i][j] = " "
    m = star(m, p)
    b = star(s[p*2:], p)
    return f + m + b

n = int(input())
s = [["*" for _ in range(n)] for _ in range(n)]
a = star(s, n)
for i in range(n):
    print(*a[i], sep="")

#-------------------------------------------

from sys import stdin
input = stdin.readline

def draw_stars(n):
  if n == 1:
    return ['*']
  stars = draw_stars(n // 3)
  L = []

  for star in stars:
    L.append(star*3)
  for star in stars:
    L.append(star + ' '*(n//3) + star)
  for star in stars:
    L.append(star*3)
  return L

N = int(input())
print('\n'.join(draw_stars(N)))