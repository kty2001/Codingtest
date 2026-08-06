# 2563 - 색종이

arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        arr[x+i][y:y+10] = [1 for _ in range(10)]
ans = 0
for a in arr:
    ans += sum(a)
print(ans)