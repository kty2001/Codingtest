def solution(citations):
    cite = sorted(citations)
    for i, c in enumerate(cite):
        if len(cite) - i <= c :
            return len(cite) - i
    return 0