# 10798 - 세로읽기

arr = []
for i in range(5):
    arr.append(list(input()))
for i in range(15):
    for j in range(5):
        try:
            print(arr[j][i], end="")
        except:
            continue