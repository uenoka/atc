# 1430_problem_A.py
def find(num):
    for i in range(num//3+1):
        endflg = False
        for j in range(num//5+1):
            for k in range(num//7+1):
                if i*3 + j*5 + k*7 == num:
                    print(i, j, k)
                    return
                if i*3 + j*5 + k*7 > num:
                    endflg = True
                    break
    print(-1)


N = int(input())
for i in range(N):
    window = int(input())
    find(window)
