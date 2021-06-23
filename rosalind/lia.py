# lia.py
# splc.py
import os
from create_fasta_data import create_fasta_data as cfd
from file_reader import readFile
from protain_translation import translate, DNAtoRNA


def solve():
    strs = readFile(os.path.basename(__file__))
    fasta_data = cfd().create_fasta_format(strs)


solve()
