# 2738 - 행렬 덧셈

n, m = map(int, input().split())
ans = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n*2):
    arr = list(map(int, input().split()))
    for j in range(m):
        ans[i % n][j] += arr[j]
for a in ans:
    print(*a)