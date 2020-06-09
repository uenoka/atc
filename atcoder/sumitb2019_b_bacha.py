# sumitb2019_b_bacha.py
N = int(input())
for i in range(50000):
    if int(i*1.08) == N:
        print(i)
        exit()
print(":(")


