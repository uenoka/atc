# abc162_d.py
n = int(input())
s = input()
r = s.count("R")
g = s.count("G")
b = s.count("B")
cnt= 0
for i in range(n):
    for j in range(i,n):
        if 2*j-i<n:
            if s[i] != s[j] and s[i] != s[2*j-i] and s[j] != s[2*j-i]:
                cnt += 1
print(r*g*b-cnt)
