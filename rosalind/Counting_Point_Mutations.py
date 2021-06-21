# Rabbits_and_Recurrence_Relations.py
import os


def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        line = file.readlines()
        print(line[0])
        print(line[1])
        return line[0], line[1]


def solve():
    s,t = readInput()
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans+=1
    return ans


print(solve())
