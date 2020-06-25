# abc035_b.py
S = input()
T = int(input())
x = 0
y = 0
cnt = 0
for c in S:
    if c=="?":
        cnt += 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1
    elif c == "L":
        x -= 1
    elif c == "R":
        x += 1
if T == 1:
    print(abs(x) + abs(y) + cnt)
else:
    print(max(abs(x) + abs(y) - cnt , len(S)%2))
