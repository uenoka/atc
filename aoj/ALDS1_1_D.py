# ALDS1_1_D.py
N = int(input())
plices = []
for _ in range(N):
    plices.append(int(input()))
profit = [0]
_min = plices[0]
_max = -100000000000
for i in range(1, N):
    _max = max(_max, plices[i]-_min)
    _min = min(_min, plices[i])
print(_max)
