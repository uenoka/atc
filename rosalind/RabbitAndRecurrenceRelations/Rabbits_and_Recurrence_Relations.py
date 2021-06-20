# Rabbits_and_Recurrence_Relations.py
import os

def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        line = file.readline().split()
        n,k = [int(n) for n in line]
        return n,k

def fib(n,k):
    if n < 3:
        memo[n] = 1
    if memo[n] == 0:
        memo[n] = fib(n-1, k)+k*fib(n-2, k)
    return memo[n]



n, k = readInput()
memo = [0]*(n+1)
print(fib(n,k))
print(memo)
