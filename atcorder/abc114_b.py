# abc114_b.py
s = input()
num = 753
m = 10**9
for i in range(len(s)-2):
    if m>abs(num-int(s[i:i+3])):
        m = abs(num-int(s[i:i+3]))
print(m)

