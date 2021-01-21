# abc180_d.py
import math
X,Y,A,B = map(int,input().split())
cnt = 0
while A*X<Y and X*(A-1)<B:
    X*=A
    cnt+=1

cnt += (Y-1-X)//B

print(cnt)
