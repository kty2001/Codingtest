def solution(scoville, K):
    import heapq
    
    answer = 0
    heapq.heapify(scoville)
    while any(s < K for s in scoville):
        if len(scoville) < 2:
            return -1
        m = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, m)
        answer += 1
        
    return answer