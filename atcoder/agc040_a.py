# agc040_a.py
S = input()
li=[]
c=""
pre = ""
for i in S:
    if pre!=i:
        
        li.append(c)
        c=""
    c+=i
    pre = i
print(li)