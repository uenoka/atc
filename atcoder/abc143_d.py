# abc143_d.py
def can_make(i,j,k):
    if L[i] < L[j] + L[k] and L[j] < L[k] + L[i] and L[k] < L[j] + L[i]:
        return True
    return False

def find(i,j,L):
    left = j
    right = N-1
    mid = (right + left)//2
    while right - left  > 1:
        mid = (right + left)//2
        print("left,mid,right",left,mid,right)
        if can_make(i,j,mid):
            print("can make")
            left = mid
        else:
            right = mid
    print("j,mid",j,mid)
    return mid-j

N = int(input())
L = list(map(int,input().split()))
cnt =0
L = sorted(L,reverse=True)
print(L)
for i in range(N):
    for j in range(i+1,N):
        print(L)
        print("i,j",i,j,L[i],L[j])
        cnt += find(i,j,L)
print(cnt)


