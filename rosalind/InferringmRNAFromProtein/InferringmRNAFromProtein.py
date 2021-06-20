'''
停止コドンのことをnoteで書いてるけど、そういうことか笑
停止コドンがないと止まらないからこのたんぱく質は生成されないと。
'''
import os

codon_count = {
    'A': 4,
    'C': 2,
    'D': 2,
    'E': 2,
    'F': 2,
    'G': 4,
    'H': 2,
    'I': 3,
    'K': 2,
    'L': 6,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 2,
    'R': 6,
    'S': 6,
    'Stop': 3,
    'T': 4,
    'V': 4,
    'W': 1,
    'Y': 2

}

def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        line = file.readline()
        return line.replace('\n','')

def solve():
    protain = readInput()
    mod = 1000000
    ans = 1
    for amin_acid in protain:
        if amin_acid=='Stop':
            break
        ans *= codon_count[amin_acid]
        ans %= mod
    ans *= 3
    ans %= mod
    print(ans)

solve()
