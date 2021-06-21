import os
from typing import Sequence

def readInput():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        return file.readlines()

def trim(str):
    return str.replace('\n', '').replace('>', '').replace(' ', '')

def prepareData(lis):
    header = trim(lis[0])
    sequence = ''
    ret = []
    for i in lis[1:]:
        if i.startswith('>'):
            ret.append((trim(header), trim(sequence)))
            header = i
            sequence = ''
        else:
            sequence += i
    ret.append((trim(header), trim(sequence)))
    header = i
    return ret

def solve():
    fasta_data = prepareData(readInput())
    print(fasta_data)
    ans = []
    for fasta1 in fasta_data:
        for fasta2 in fasta_data:
            if fasta1==fasta2:
                continue
            if fasta1[1][-3:] == fasta2[1][:3]:
                ans.append((fasta1[0], fasta2[0]))
    for i in ans:
        print(i[0],i[1])
solve()
