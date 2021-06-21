# splc.py
import os
from create_fasta_data import create_fasta_data as cfd
from file_reader import readFile
from protain_translation import translate, DNAtoRNA


def splicing(fasta_data):
    sequence = fasta_data[0][1]
    for intron in fasta_data[1:]:
        sequence = sequence.replace(intron[1], '')
    return sequence
def solve():
    strs = readFile(os.path.basename(__file__))
    fasta_data = cfd().create_fasta_format(strs)
    sequence = splicing(fasta_data)
    sequence = DNAtoRNA(sequence)
    ans = translate(sequence)
    print(ans)

solve()
