# ITP1_7_B.py
while True:
    ans = 0
    N, X = map(int,input().split())
    if N==0 and X == 0:
        break
    for i in range(1,N+1):
        for j in range(i+1,N):
            k = X - i - j
            if k > i and k > j and N >= k > 0:
                ans+=1
    print(ans)