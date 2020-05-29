#abc116 c
def is_same(m):
    print("len is",len(list(set(m))))
    return len(list(set(m))) == 1
N = int(input())
#print(N)
M = list(map(int,input().split()))
ans = 0
highest = max(M)
tmp = []
f = [0]*N
while not is_same(M,F):
    print("")
print(ans)