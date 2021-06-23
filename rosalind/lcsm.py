# Finding a Shared Motif

from protain_translation import translate, DNAtoRNA
from file_reader import readFile
from create_fasta_data import create_fasta_data as cfd
import os


def findLCString(fasta):
    pass


def solve():
    strs = readFile(os.path.basename(__file__))
    fasta_data = cfd().create_fasta_format(strs)
    ans = findLCString(fasta_data)

solve()

