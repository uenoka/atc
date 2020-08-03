# keyence2019_c.py
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if sum(A)<sum(B):
    print(-1)
    exit()

C = []
diff = 0
cnt = 0
for i in range(N):
    d = A[i] - B[i]
    if d < 0:
        cnt += 1
        diff += d
    else:
        C.append(d)
C.sort(reverse=True)
for i in C:
    if diff >= 0:
        break 
    diff += i
    cnt+=1
print(cnt)