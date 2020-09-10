# abc175_b.py
N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i]!=L[j] and L[k]!=L[j] and L[i]!=L[k]:
                if L[i] + L[j] > L[k] and L[k] + L[j] > L[i] and L[i] + L[k] > L[j]:
                    ans +=1
                    # print(L[i] , L[j] , L[k],"///",i,j,k)
print(ans)