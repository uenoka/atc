import os

def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        line = file.readline()
        return int(line)

def calc_len(n):
    ans = 1
    for i in range(1,n+1):
        ans*=i
    return ans

def solve():
    import itertools
    N = readInput()
    l = [i+1 for i in range(N)]
    target =  itertools.permutations(l)
    print(calc_len(N))
    for perm in list(target):
        for i in perm:
            print(i,end=' ')
        print()

solve()
