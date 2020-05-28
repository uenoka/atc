# ALDS1_5_A.py
def rec(m, use, idx):
    if idx<=len(A):
        if sum(use)==m:
            return True
        use.push(A[idx+1])
        rec(m,use,idx+1)
        use.pop()
        rec(m,use,idx+1)
    


N = int(input())
A = list(map(int, input().split()))
M = list(map(int, input().split()))

print(rec(M[0], [],0))
