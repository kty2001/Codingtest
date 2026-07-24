def solution(phone_book):
    answer = True
    phone = sorted(phone_book)
    for i in range(len(phone)-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            return False
    return answer