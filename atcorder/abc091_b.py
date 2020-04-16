#abc091_b
import collections
N = int(input())
S = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]
S_c = collections.Counter(S)
T_c = collections.Counter(T)
ans = 0

for s_word,s_count in S_c.items():
    if ans < s_count-T_c[s_word]:
        ans = s_count-T_c[s_word]

print(max(ans,0))