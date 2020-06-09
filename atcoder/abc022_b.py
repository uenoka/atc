# abc022_b.py
flower = [0]*(10**5+1)
N = int(input())
A = [int(input()) for i in range(N)]
for i in A:
    flower[i] +=1
ans = 0
for i in flower:
    if i > 1:
        ans+=i-1
print(ans)