# ALDS1_10_A.py
N = int(input())
fib_list = [0]*(N+1)
def fib(n):
    if n<=1:
        fib_list[n] = 1
    else:
        if fib_list[n] == 0:
            fib_list[n] = fib(n-1) + fib(n-2)
    return fib_list[n]
fib(N)
print(fib_list[N])
