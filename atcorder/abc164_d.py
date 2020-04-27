# abc164_d.py
'''
len(S)=20000 なので N^2 が間に合わない。
最低 NlogN にしたいがどうするか…
なんとなく尺取り法っぽい…？
想定解は動的計画法。
'''
S = input()
ans = 0
for i in range(len(S)):
    for j in range(i+3,len(S)):
        if (int(S[i:j+1]))%2019 == 0:
            ans+=1
print(ans)

left=0
right=len(S)-1
while left<right:
    num = S[left:right]
    if num%2019 == 0:
        ans+=1
    
