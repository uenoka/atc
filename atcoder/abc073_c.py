# abc073_c.py
N = int(input())
A = [int(input()) for i in range(N)]
ans = set()
for i in A:
    if i in ans:
        ans.discard(i)
    else:
        ans.add(i)
print(len(ans))