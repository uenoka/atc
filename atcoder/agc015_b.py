import collections
N = int(input())
A = list(map(int,input().split()))

C = collections.Counter(A)
#print(C)
calc = {}
for i,cnt in C.items():
    calc[i] = cnt*(cnt-1)//2
#print("calc:",calc)
calc_sum = sum(calc.values())
for i in range(N):
    ans = calc_sum - calc[A[i]]
#    print("ans",ans)
#    print("A[i]",A[i],"calc[A[i]]",calc[A[i]])
    if calc[A[i]] != 0:
        ans += (C[A[i]]-1)*(C[A[i]]-2)//2
#        print((calc[A[i]]-2)*(calc[A[i]]-1)//2)
#        ans += (calc[A[i]]-2)*(calc[A[i]]-1)//2
    print(ans)
