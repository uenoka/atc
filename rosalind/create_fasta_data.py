# create_fasta_data.py
'''
input  : fasta format string strst
output : strst like this [(header,sequence)]
'''


class create_fasta_data():
    def trim(self,str):
        return str.replace('\n', '').replace('>', '').replace(' ', '')

    def create_fasta_format(self, strs):
        header = self.trim(strs[0])
        sequence = ''
        ret = []
        for i in strs[1:]:
            if i.startswith('>'):
                ret.append((self.trim(header), self.trim(sequence)))
                header = i
                sequence = ''
            else:
                sequence += i
        ret.append((self.trim(header), self.trim(sequence)))
        return ret
