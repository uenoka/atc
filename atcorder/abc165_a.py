# abc165_a.pynin
N = int(input())
A, B = map(int,input().split())
for i in range(A,B+1):
    if i%N == 0:
        print('OK')
        exit()
print("NG")
