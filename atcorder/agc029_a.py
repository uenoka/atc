# agc029_a.py
# W の後ろに何個Bがあるかをカウントすれば行けそう
cnt = 0
S = input()
bcnt = 0
ans = 0
for i in S:
    if i =="B":
        bcnt +=1
    else:
        ans += bcnt
print(ans)