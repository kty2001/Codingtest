def solution(wallpaper):
    answer = []
    y_s = 51
    x_s = 51
    y_e = 0
    x_e = 0
    for i, w in enumerate(wallpaper):
        if w.find('#') != -1:
            y_s = min(y_s, i)
            x_s = min(x_s, w.find('#'))
            y_e = max(y_e, i)
            x_e = max(x_e, len(w) - w[::-1].find('#'))
    return [y_s, x_s, y_e+1, x_e]