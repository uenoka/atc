#abc098_b
def compare(str1,str2):
    ans = 0
    str1=''.join(set(str1))
    str2=''.join(set(str2))
    for c in str1:
        ans += str2.count(c)

    return ans

N = int(input())
S = input()
m = 0
for i in range(N):
#    print(S[:i],S[i:])
    tmp = compare(S[:i],S[i:])
    if m < tmp:
        m=tmp
print(m)