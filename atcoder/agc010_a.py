# agc010_a.py
N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in A:
    if i % 2 == 1:
        cnt += 1
if cnt % 2 == 1:
    print('NO')
else:
    print('YES')
