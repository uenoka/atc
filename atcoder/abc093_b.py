# abc093_b.py
A, B,K = map(int,input().split())
ans = []
for i in range(K):
#    print(i)
    ans.append(i+A)
    if i >(B-A-1):
        break
for i in range(K):
#    print(A-i)
#    print(i)
    ans.append(B-i)
    if i >(B-A-1):
        break
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)