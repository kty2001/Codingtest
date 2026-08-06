# 3052 - 나머지

arr = []
for _ in range(10):
    arr.append(int(input()) % 42)
print(len(set(arr)))