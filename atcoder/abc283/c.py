s = input()
ans = 0
idx = 0 
while idx < len(s):
    if s[idx]== '0' and idx < len(s)-1 and s[idx+1] == '0':
        idx += 1
    ans += 1
    idx += 1
print(ans)