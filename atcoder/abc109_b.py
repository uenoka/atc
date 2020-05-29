# abc109_b.py
N = int(input())
W = [input() for i in range(N)]
pre =""
for word in W:
    if W.count(word)>1 or (pre[-1:]!=word[0] and pre!=""):
        print('No')
        exit()
    pre = word
print('Yes')
