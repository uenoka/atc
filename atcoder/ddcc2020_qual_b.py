# ddcc2020_qual_b.py
'''
diff をそれぞれの切れ目での左右の長さの差の絶対値として、その最小値を求める。
（中心近くの切れ目2つで比較すればよさそうだが、長さがちょうど半分になる場合
や偶奇で面倒だったのでこの方法にした。）
想定解は累積和だったが、考え方は似ている。（自分の回答は左右の差をじかに見ていて、
想定解は sum(B1,Bs)-sum(Bs+1 ,Bn) の sum(B1,Bs), sum(Bs+1 ,Bn) をそれぞれ求めている。）
'''
N = int(input())
A = list(map(int,input().split()))
_sum = sum(A)
diff = [0]*(N-1)
cumul = 0
for i in range(N-1):
    cumul += A[i]
    diff[i] = abs(cumul - (_sum - cumul))
# print(diff)
print(min(diff))

