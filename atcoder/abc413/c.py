
Q = int(input())
A = []
idx = 0
for _ in range(Q):
    q = input().split()
    querytype = int(q[0])
    if querytype==1:
        A.append([int(q[1]),int(q[2])])
    else:
        ans = 0
        k = int(q[1])
        while k > 0:
            if k >= A[idx][0]:
                ans += A[idx][1] * A[idx][0]
                k -= A[idx][0]
                idx += 1
            else:
                ans += A[idx][1] * k
                A[idx][0] -= k
                break
        print(ans)
