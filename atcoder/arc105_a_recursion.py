# arc105_a_recursion.py
'''
200 点だけどBit全探索の問題。
普通に難しいと感じた。。。
ただ、どんなに頑張っても16パターン（2^4）なのでどうにかすればできるという意味では教育的な問題なのかも。
Bit全探索を誰かに教える場合は、この問題を最初に解かせるかもなぁ。

解法としては
・ソートしても問題ない（ソートすることで大小関係が明確になる。 A<=B<=C<=D の時明らかにA=B+C+D ということはあり得ないので、答えがA+B=C+D or A+B+C=D になる）のでソートして解く（想定解法）
・Bit全探索で解く
  ・4桁の0，1の配列を用意（[0,0,0,0]~[1,1,1,1]）して、各配列で各要素とa,b,c,dを掛けて、合計の半分になるか判定
  ・BFSでaを使う、使わない、bを使う、使わない…と探索して行く
'''


def solve_by_bits(b, A):
    if len(b) == 4:
        sums = sum(A)
        ans = 0
        for i in range(4):
            ans += A[i]*b[i]
        if sums/2 == ans:
            print('Yes')
            exit()
        else:
            return
    for i in range(2):
        b.append(i)
        solve_by_bits(b, A)
        b.pop()


def bit_search_solution():
    A = list(map(int, input().split()))
    solve_by_bits([], A)
    print('No')


bit_search_solution()
