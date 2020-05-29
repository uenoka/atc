# abc127_b.py
def rec(Xi,cnt):
    if cnt>=10:
        return

    Xnext = r*Xi-D
    print(Xnext)
    rec(Xnext,cnt+1)

r,D,x = map(int,input().split())
rec(x,0)
