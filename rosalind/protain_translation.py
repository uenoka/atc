# protain_translation.py
import codon_table
def translate(seq):
    mapping = codon_table.rna_to_protain
    idx = 0
    ans = ''
    while idx < len(seq)-3:
        codon = seq[idx:idx+3]
        if mapping[codon] == 'Stop':
            return ans
        if codon not in mapping:
            return ans
        ans += mapping[codon]
        idx += 3
    return ans


def transcript(DNA):
    RNA = ''
    for base in DNA:
        RNA+=codon_table.dna_to_rna[base]
    return RNA


def DNAtoRNA(DNA):
    return DNA.replace('T', 'U')
