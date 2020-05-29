# ALDS1_13_A.py
def printans():
    for i in ans:
        print("".join(i))

N = int(input())
Q = []
for i in range(N):
    Q.append(list(map(int,input().split())))
ans = [["."]*8 for i in range(8)]
for i in Q:
    ans[i[0]][i[1]] = "Q"



printans()
