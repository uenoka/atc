# abc038_c.py
N = int(input())
A = list(map(int, input().split()))
right = 0
cnt = 0
pre = 0
for left in range(N):
    while right < N and (right == left or pre < A[right]):
        pre = A[right]
        right += 1
    cnt += right - left
    if right == left:
        right += 1
print(cnt)
