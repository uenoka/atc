import os

def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        line = file.readlines()
        print(line[0])
        print(line[1])
        return line[0].replace('\n', ''), line[1].replace('\n', '')


def solve():
    s, t = readInput()
    ans = []
    length = len(t)
    for i in range(len(s)):
        # print('=========')
        # print(t)
        # print(s[i:i+length])
        if s[i:i+length] == t:
            ans.append(i)
    return ans


ans = solve()
for i in ans:
    print(i+1,end=' ')
