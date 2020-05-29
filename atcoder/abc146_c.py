# abc146_c.py
def is_ok(A,B,mid,X):
########## wirte criteria here ##########
    if  A*mid + B*len(str(mid)) > X:
#        print("A * N + B * d (N) = ",A*mid + B*len(str(mid)))
        return True
    return False

def meguru_bisect(A,B,X):
    left = 0
    right = 10**9+1
    while (abs(right - left) > 1):
        mid = left + (right - left) // 2
        if is_ok(A,B,mid,X):
            right = mid
#            print("right : mid : ",mid)
        else:
            left = mid
#            print("left : mid : ",mid)
    return left

A,B,X = map(int,input().split())
print(meguru_bisect(A,B,X))
