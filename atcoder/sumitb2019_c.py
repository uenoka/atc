# bsumitb2019_c.py

X = int(input())
head = X//100
tail = X%100
if tail >head*5:
    print(0)
else :
    print(1)