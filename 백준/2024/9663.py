# 9663 - N-Queen

#----------------------------------

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    
    for i in range(n):
        row[x] = i
        for j in range(x):
            if row[x] == row[j] or abs(row[x] - row[j]) == abs(x - j):
                break
        else:
            n_queens(x+1)

n = int(input())
ans = 0
row = [0] * n
n_queens(0)
print(ans)