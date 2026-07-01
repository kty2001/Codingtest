def solution(data, ext, val_ext, sort_by):
    edic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ans = []
    for d in data:
        if d[edic[ext]] < val_ext:
            ans.append(d)
    ans = sorted(ans, key=lambda x: x[edic[sort_by]])
    return ans