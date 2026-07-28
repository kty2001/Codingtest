def solution(people, limit):
    answer = 0
    boat = 0
    front, rear = 0, len(people) - 1
    people = sorted(people, reverse=True)
    while front <= rear:
        if front == rear:
            return answer + 1
        
        boat = people[front]
        if boat + people[rear] <= limit:
            rear -= 1
        front += 1
        answer += 1
    return answer