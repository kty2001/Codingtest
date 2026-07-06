def solution(new_id):
    answer = ''
    n_id = ''
    right = ['-', '_', '.']
    new_id = new_id.lower()
    for n in new_id:
        if n in right or n.isdigit() or (ord(n) <= 122 and ord(n) >= 97):
            answer += n
    for a in answer:
        if n_id[-1:] == '.' and a == '.':
            continue
        n_id += a
    print(n_id)
    new_id = n_id.strip('.')
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id