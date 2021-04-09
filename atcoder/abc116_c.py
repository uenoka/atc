# abc116 c
N = int(input())
A = list(map(int, input().split()))
cnt = 0
for _ in range(max(A)):
    cnt += 1
    for i in range(N):
        if A[i] <= 0 and (i != 0 or i != N-1) and A[i+1] > 0:
            cnt += 1
        A[i] -= 1
        print(i, cnt)
    print(A)
print(cnt)
