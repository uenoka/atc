# abc180_b.py
import math

def manhatten(a):
    ans = 0
    for i in a:
        ans+=abs(i)
    return ans

def eucrid(a):
    ans = 0
    for i in a:
        ans+=(i**2)
    return (ans**0.5)

def chep(a):
    m = 0
    for i in a:
        if abs(i)>m:
            m=abs(i)
    return m

N = int(input())
A = list(map(int,input().split()))
print(manhatten(A))
print(eucrid(A))
print(chep(A))

