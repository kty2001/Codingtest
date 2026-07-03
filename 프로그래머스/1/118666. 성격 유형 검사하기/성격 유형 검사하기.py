def solution(survey, choices):
    answer = ''
    cha = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        if choices[i] == 4:
            pass
        elif choices[i] < 4:
            cha[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            cha[survey[i][1]] += choices[i] - 4
    if cha['R'] >= cha['T']:
        answer += 'R'
    elif cha['R'] < cha['T']:
        answer += 'T'
    if cha['C'] >= cha['F']:
        answer += 'C'
    elif cha['C'] < cha['F']:
        answer += 'F'
    if cha['J'] >= cha['M']:
        answer += 'J'
    elif cha['J'] < cha['M']:
        answer += 'M'
    if cha['A'] >= cha['N']:
        answer += 'A'
    elif cha['A'] < cha['N']:
        answer += 'N'
    return answer