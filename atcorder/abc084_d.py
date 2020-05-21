# abc084_d.py
'''
毎回素数判定するとTLEしてしまう。（計算量は O(Q) × 2 × O((R-L)log(log (R-L)))) × ? ）
（Q 回クエリが投げられて、それぞれ R-L 個の数字に対して素数判定を 2 回行う、ということを言いたい）
そのため、一度すべての範囲で Like Number を判定しておいて、
自分までに何個の Like Number があったかを配列にもたせて累積和で回答をする。
そうすることによって、累積和の事前準備に O(Nlog(logN)), 実際の計算に O(1) となる。


'''
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def is_like_num(n):
    return is_prime(n) and is_prime((n+1)//2)

erast_list =[0]*100001
cnt = 0
for i in range(100001):
    if is_like_num(i):
        cnt+=1
    erast_list[i] = cnt
# print(erast_list[:5])
Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
#    print(erast_list[R+1],erast_list[L-1])
    print(erast_list[R+1]-erast_list[L-1])