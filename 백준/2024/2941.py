# 2941 - 크로아티아 알파벳

w = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in cro:
    w = w.replace(c, "$")
print(len(w))