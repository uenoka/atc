# abc104_b.py
S = input()
upper_cnt=0
for i,c in enumerate(S):
    if (i==0 and c!="A") or S[2:-1].count("C")!=1 or (i==1 and not c.islower()):
        print('WA')
        exit()
    if i>=1 and c.isupper():
         upper_cnt+=1
    if upper_cnt >1:
        print('WA')
        exit()
print('AC')

