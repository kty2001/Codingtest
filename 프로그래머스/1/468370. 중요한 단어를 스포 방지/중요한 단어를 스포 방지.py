def solution(message, spoiler_ranges):
    spo = []
    words = set(message.split())
    message = list(message)
    
    for s in spoiler_ranges:
        spo += [i for i in range(s[0], s[1] + 1)]
    
    for i in range(len(message)):
        if message[i] != ' ' and i in spo:
            message[i] = '*'
    message = ''.join(message)
    spo_words = set(message.split())
    spo_words = words - spo_words
    
    return len(spo_words)