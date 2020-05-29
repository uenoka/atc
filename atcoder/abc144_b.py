#abc144_b.py
N = int(input())
ans = "No"
for i in range(1,10):
    for j in range(1,10):
        if N==j*i:
            ans ="Yes"
            print(ans)
            exit()
print(ans)