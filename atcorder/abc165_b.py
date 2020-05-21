# abc165_b.py
X = int(input())
a = 100
r = 0.01
for i in range(1000000):
    a = int(a*(1+r))
    if a >= X:
        print(i+1)
        exit()
    
