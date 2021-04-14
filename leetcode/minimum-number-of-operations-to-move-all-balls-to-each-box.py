# minimum-number-of-operations-to-move-all-balls-to-each-box
'''
答えを出すだけなら簡単だったが、計算量的にはO(N^2)になる。
O(N) 解法は左右で累積和を取っていき、左右の同じインデックス同士で足し合わせるというもの。
left/rightCount = 今いる場所より左 or 右にあるボールの数を表す
left/rightCost = 今いる場所に左 or 右からボールを移動するコストを表す
たとえば入力が"1000"の場合、それぞれ
leftCount  = [0,1,1,1] (左側にあるボールの数のため、2つめ以降で 1 になる)
rightCount = [0,0,0,0] (右側にあるボールの数のため、どこも 0 になる)
leftCost   = [0,1,2,3] (左側のボールを1つずつ動かすコストのためこのようになる)
rightCost  = [0,0,0,0] (右側にはボールがないため) 
各箱に移すコストは left/rightCost の各インデックスでの値を足し合わせたものと同値になる（それぞれが左から動かしたコストと右から動かしたコストを表すため）
2回累積和をとるだけでこんな計算量改善できるのすげー
'''
class Solution:
    def minOperations(self, boxes: str):
        idx = [i for i in range(len(boxes)) if boxes[i] == "1"]
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            for j in idx:
                ans[i] += abs(i-j)
        return ans

    def minOperations2(self, boxes: str):
        ans = [0]*len(boxes)
        cumsum = 0
        leftCount = [0]*len(boxes)
        for i in range(len(boxes)):
            leftCount[i]=cumsum
            cumsum += 1 if boxes[i]=="1" else 0
        print(leftCount)
        cumsum = 0
        leftCost = [0]*len(boxes)
        for i, v in enumerate(leftCount):
            cumsum += v
            leftCost[i] = cumsum
        print(leftCost)
        rightCount = [0]*len(boxes)
        cumsum = 0
        for i in range(1,len(boxes)+1):
            rightCount[-i] = cumsum
            cumsum += 1 if boxes[-i] == "1" else 0
        rightCount.reverse()
        print(rightCount)
        cumsum = 0
        rightCost = [0]*len(boxes)
        for i,v in enumerate(rightCount):
            cumsum += v
            rightCost[i] = cumsum
        print(rightCost)
        rightCost.reverse()
        for i in range(len(boxes)):
            ans[i]=rightCost[i]+leftCost[i]
        return ans

testcases =[
    "11010"
]
for boxes in testcases:
    sol = Solution().minOperations2(boxes)
    print(sol)
