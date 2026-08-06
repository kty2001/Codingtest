# 25206  - 너의 평점은

grade = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
score = []
cnt = 0
for _ in range(20):
    info = input().split()
    if info[2] == "P":
        continue
    else:
        score.append(float(info[1]) * grade[info[2]])
        cnt += float(info[1])
print(sum(score) / cnt)
