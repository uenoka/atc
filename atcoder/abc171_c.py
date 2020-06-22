# abc171_c.py
import math
N = int(input())
ans=[]
while N > 0:
    ans.append(N%26)
    N = math.floor((N-1)/26)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = reversed(ans)
for i in ans:
    print(alphabet[i-1],end="")
