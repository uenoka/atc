# abc086_b.py
A, B = map(int,input().split())
for i in range(1000):
    if (10**len(str(B)) * A + B) == i**2:
        print('Yes')
        exit()
    
print('No')
