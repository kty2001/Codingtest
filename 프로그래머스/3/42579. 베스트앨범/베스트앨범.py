def solution(genres, plays):
    answer = []
    play = {i: p for i, p in enumerate(plays)}
    genre = {}
    for i, g in enumerate(genres):
        if g not in genre:
            genre[g] = [play[i], {i: play[i]}]
        else:
            genre[g][0] += play[i]
            genre[g][1][i] = play[i]
    for g in sorted(genre, key=lambda x: genre[x][0], reverse=True):
        l = sorted(genre[g][1], key=lambda x: genre[g][1][x], reverse=True)
        answer += l[:2]
    return answer