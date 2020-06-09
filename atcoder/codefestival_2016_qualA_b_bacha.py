# codefestival_2016_qualA_b_bacha.py
N = int(input())
A = list(map(int,input().split()))
ans = 0
for i,v in enumerate(A):
    # print(i ,v, A[v-1])
    if i+1 == A[v-1]:
        ans += 1
print(ans//2)