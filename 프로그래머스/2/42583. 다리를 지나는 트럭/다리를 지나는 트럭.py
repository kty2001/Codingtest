def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []
    t = []
    while stack or truck_weights:
        if not stack:
            stack.append(truck_weights.pop(0))
            t.append(answer)
            
        else:
            if t and t[0] + bridge_length == answer:
                stack.pop(0)
                t.pop(0)
            if truck_weights and len(stack) < bridge_length and sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
                t.append(answer)

        answer += 1
            
    return answer