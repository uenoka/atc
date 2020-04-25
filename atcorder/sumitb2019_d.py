# sumitb2019_d.py
'''
重複考えないとどうなるか
-> 単に nC3 個( N 個から 3 つ選び出す順列と同じ)
というところまで考えたが、結局わからず解説AC
重複を考えるとかなり厳しいので重複がないものに着目する。
（今回であれば 000~999 までのパスワード）
発想の転換が凄い。これ思いつくの天才だろ…。
'''
N = int(input())
S = input()
cnt = 0
for i in range(1000):
    C = [str(i//100), str(i//10%10), str(i%10)]
    f = 0
    for s in S:
        if s == C[f]:
            f += 1
        if f == 3:
           break
    if f == 3:
        cnt += 1
    if cnt ==1000:
        break
print(cnt)
