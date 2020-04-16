
# abc068_b.py
N = int(input())
binaries = [2,4,8,16,32,64]
ans = 1
for i in binaries:
    if N>=i:
        ans=i
print(ans)
