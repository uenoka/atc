# make-two-arrays-equal-by-reversing-sub-arrays.py
'''
珍しく考察系問題。
キモは「ある配列から同じ要素を持った任意の並びの配列が逆順にすることで生成できるかどうか」かな。
もし出来るなら要素を比較すればいいだけで、出来ないなら何かしらシミュレーションしないといけない。
→できる。
まず 2 要素の配列 [a,b] から [b,a] は自明に作成が可能
次に 3 要素の配列を考えると 3 要素の配列は [a , b, c] となる。
この時に [b, c] = B とすると、[a, B] と表現でき、この配列は全要素を生成が可能。
また B の内部である [b, c] においても全要素が生成可能。
このような操作は再帰的に4, 5, ... N 要素においても全要素が生成可能となる。
（もうちょっと数学的帰納法的な書き方出来たらいいな）

解法自体はソートする、dict に入れて同じ数あるかどうかを確認する等がある。
'''


class Solution:
    def canBeEqual(self, target, arr) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if target[i] != arr[i]:
                return False
        return True

    def canBeEqual2(self, target, arr) -> bool:
        import collections
        targetCollection = collections.Counter(target)
        arrCollection = collections.Counter(arr)
        return targetCollection == arrCollection


sol = Solution()
target = [5, 6, 3, 2, 1]
arr = [1, 2, 3, 4, 5]
print(sol.canBeEqual(target, arr))
