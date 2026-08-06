# 4779 - 칸토어 집합

import sys

def c(s):
    p = len(s)//3
    if p == 0: return s
    f = c(s[:p])
    m = " " * p
    b = c(s[p*2:])
    return f + m + b

while True:
    try: n = int(sys.stdin.readline())
    except: break
    s = "-" * 3**n
    print(c(s))

#---------------------------------

import sys

def delete(string):
  if string == '-' or string == ' ':
    return string
  else:
    a = len(string) // 3
    str1, str2= '-'*a, ' '*a
    ds1 = delete(str1) 
    return ds1 + str2 + ds1

while True:
  n = sys.stdin.readline().rstrip()
  if n == '':
    break
  else:
    line = '-'* 3**int(n)
    print(delete(line))