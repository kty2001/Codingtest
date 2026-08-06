# 1316 - 그룹 단어 체커

n = int(input())
cnt = 0
for i in range(n):
    word = input()
    arr = []
    for w in word:
        if w not in arr:
            arr.append(w)
        else:
            if w == arr[-1]:
                continue
            else:
                break
    else:
        cnt += 1
print(cnt)