import os

def solve():
    dir = os.path.dirname(__file__)
    file = os.path.join(dir, 'rosalind.txt')
    with open(file, "r") as file:
        lines = file.read().split('\n')
        ret = []
        seq = ''
        cnt = 0
        number = ''
        for line in lines:
            if line.startswith('>'):
                if cnt != 0:
                    ret.append((number,seq))
                seq = ''
                number = line
            else:
                seq += line
            cnt += 1
        # ret.append((number, seq))
        ans = (0,0)
        for n,s in ret:
            total = len(s)
            gc_cnt = s.count('C')+s.count('G')
            if ans[1]<(gc_cnt)*100/total:
                ans = (n, (gc_cnt)*100/total)
        print(ans)





solve()
