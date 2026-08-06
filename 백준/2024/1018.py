# 1018 - 체스판 다시 칠하기

n, m = map(int, input().split())
b = ["W", "B"]
c = []
for i in range(n):
    c.append(list(input()))
ans = 64
for i in range(n-7):
    for j in range(m-7):
        p = 0
        q = 0
        for x in range(8):
            a = c[i+x][j:j+8]
            for y in range(8):
                if a[y] != b[(x+y)%2]:
                    p += 1
                if a[y] != b[(x+y+1)%2]:
                    q += 1
        ans = min(ans, p, q)
print(ans)