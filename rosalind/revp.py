# revp.py

# Locating Restriction Sites
'''
制限酵素でカットされるサイト（4~12bpの回文になっている箇所）を探して、
スタート位置と長さを返す。
基本的には端から4bp見ていって、回文を見つけたら両端を増やして回文かどうかを判定するという流れでよさそう。
（回文の中身は回文になっているため。）
LeetCodeでも類似の問題見たからそれも復習しておくとよいかな。
制限酵素の切断だから基本的には偶数個でよいはずだけどそこは問題文にある？？
'''
from protain_translation import translate, DNAtoRNA
from file_reader import readFile
from create_fasta_data import create_fasta_data as cfd
from codon_table import DNA_base_pair as pair
import os

def isPair(s,t):
    return pair[s] == t


def isPalindrome(seq):
    for i in range(len(seq)):
        if not isPair(seq[i],seq[-i-1]):
            return False
    print('seq',seq,'is palindrome')
    return True

def findPalindromes(idx,seq):
    ret = []
    start = idx
    end = idx + 4
    while start >= 0 and end <= len(seq) and end-start <= 12 and isPalindrome(seq[start:end]):
        ret.append((start+1,end-start))
        start -= 1
        end += 1
    return ret

    

def solve():
    strs = readFile(os.path.basename(__file__))
    sequence = cfd().create_fasta_format(strs)[0][1]
    ans = []
    for i in range(len(sequence)):
        palindromes = findPalindromes(i,sequence)
        ans += palindromes
    ans.sort()
    for i in ans:
        for j in i:
            print(j,end=' ')
        print()

solve()
