N = int(input())
A = list(map(int, input().split()))
D = int(input())
Lmax = [0]
current_max = 0
for a in A:
    if a > current_max:
        current_max = a
    Lmax.append(current_max)
Rmax = [0]
current_max = 0
for a in reversed(A):
    if a > current_max:
        current_max = a
    Rmax.append(current_max)
for i in range(D):
    L,R = map(int,input().split())
    ans = max(Lmax[L-1], Rmax[N-R])
    print(ans)