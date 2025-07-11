N = int(input())
while N%3 == 0:
    N//=3
while N%2 == 0:
    N//=2
if N==1:
    print('Yes')
else:
    print('No')