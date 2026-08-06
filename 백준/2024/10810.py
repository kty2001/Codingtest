# 10810 - 공 넣기

n, m = map(int, input().split())
arr = [0 for _ in range(n+1)]
for _ in range(m):
    i, k, j = map(int, input().split())
    arr[i:k+1] = [j for _ in range(k-i+1)]
print(*arr[1:])