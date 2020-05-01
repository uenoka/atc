# codefestival_2016_qualA_b.py
'''
A[Ai] == i をカウントする。このときお互いに参照しあうため、答えはカウントの半分になる。
'''

N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i,v in enumerate(A):
    if A[v-1] == i+1:
        cnt += 1
print(cnt//2)