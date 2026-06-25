def solution(friends, gifts):
    arr = [[0 for _ in range(len(friends)+2)] for _ in range(len(friends))]
    for gift in gifts:
        a, b = gift.split()
        arr[friends.index(a)][friends.index(b)] += 1
        
    for i in range(len(friends)):
        arr[i][-2] = sum(arr[i])
        for j in range(len(friends)):
            arr[i][-2] -= arr[j][i]
        
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j: continue
            elif arr[i][j] > arr[j][i]:
                arr[i][-1] += 1
            elif arr[i][j] == arr[j][i] and arr[i][-2] > arr[j][-2]:
                arr[i][-1] += 1
    
    answer = 0
    for i in arr:
        answer = max(answer, i[-1])
        
    return answer