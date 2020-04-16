# abc088_b.py
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
alice = []
bob = []
for i,v in enumerate(A):
    if i%2==0:
        alice.append(v)
    else:
        bob.append(v)
print(sum(alice)-sum(bob))
