# babc170_b.py
X, Y = map(int,input().split())
for i in range(1000):
    for j in range(1000):
        if i+j==X and i*2 + j * 4==Y:
            print('Yes')
            exit()
print('No')