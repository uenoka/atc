# cons.py
import os
from create_fasta_data import create_fasta_data as cfd
from file_reader import readFile
from protain_translation import translate, DNAtoRNA
import collections

def findComonAncestor(fasta_data):
    sequence = [fasta[1] for fasta in fasta_data]
    counters = []
    for i in range(len(sequence[0])):
        counter = collections.Counter()
        for seq in sequence:
            if seq[i] in counter:
                counter[seq[i]] += 1
            else:
                counter[seq[i]] = 1
        counters.append(counter)
    comonn_ancestor = ''.join([c.most_common(1)[0][0] for c in counters])
    codon_counter = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }
    codon = 'ATGC'
    for counter in counters:
        for c in codon:
            if c in counter:
                codon_counter[c].append(counter[c])
            else:
                codon_counter[c].append(0)
    return (comonn_ancestor,codon_counter)

def solve():
    strs = readFile(os.path.basename(__file__))
    fasta_data = cfd().create_fasta_format(strs)
    ans = findComonAncestor(fasta_data)

    file_name = os.path.basename(__file__).replace('.py', '')
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind_'+file_name+'_output.txt')
    with open(file, "w") as f:
        f.write(ans[0]+'\n')
        for i in ans[1].items():
            counter = [str(c) for c in i[1]]
            f.write(i[0]+': ' + ' '.join(counter) +'\n')

solve()
