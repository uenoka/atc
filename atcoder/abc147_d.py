
# abc147_d.py
'''
単純にやろうと思うと、O(N!) かかってしまう + mod をとるのが難しい、という問題。
-> mod のほうは逆元を知っていればできる
-> O(N!) のほうは XOR の性質を考えていかに計算が楽になるかを考察する。
という（ある程度の）典型の組み合わせ問題。
入力がたとえば
6
a b c d e f
だとすると
a^b + a^c + a^d + a^e + a^f + b^c + b^d + b^e + b^f + c^d + c^e + c^f + d^e + d^f + e^f
'''

# permutation を適切な形に修正できれば通るはず -> how ?


def permutation():
    ans = 0
    for i in range(0, N):
        for j in range(i, N):
            if i != j:
                print(A[i], A[j])
                ans += A[i] ^ A[j]
                ans %= mod
    return ans


mod = 10**9+7
N = int(input())
A = list(map(int, input().split()))
print(permutation())
