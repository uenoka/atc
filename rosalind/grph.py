import os
from typing import List
from create_fasta_data import create_fasta_data as cfd
from file_reader import readFile


def solve():
    strs = readFile(os.path.basename(__file__))
    fasta_data = cfd().create_fasta_format(strs)
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
