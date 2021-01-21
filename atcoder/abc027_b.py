# abc027_b.py

N = int(input())
A = list(map(int, input().split()))
if not sum(A) % N == 0:
    print(-1)
    exit()

target = sum(A)//N

cumsum = 0
counter = 0
bridge = 0
for i in A:
    cumsum += i
    counter += 1
    if cumsum/counter == target:
        cumsum = 0
        counter = 0
    else:
        bridge += 1
print(bridge)
