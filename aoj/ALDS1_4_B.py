# ALDS1_4_B.pys

def is_ok(idx,key,target):
########## wirte criteria here ##########
    if target[idx] >= key:
        return True
    return False

def meguru_bisect(key,target):
    left = -1
    right = len(target)
    while (abs(right - left) > 1):
        mid = left + (right - left) // 2
        if is_ok(mid,key,target):
            right = mid
        else:
            left = mid
    if key == target[right]:
        return True
    return False

N = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))
ans = 0
for i in T:
    if meguru_bisect(i,S):
        ans += 1
print(ans)
