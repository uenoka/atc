# scontainer-with-most-water.py
'''
まずは愚直な2重ループで実装してみる。
他の解法として何があるか？
Two pointers の両端スタートでできる
ただしこれの正当性が良くわかっていないので↓を読み込む
https://leetcode.com/problems/container-with-most-water/discuss/200246/Proof-by-formula 
'''
class Solution:
    def maxArea(self, height) -> int:
        return self.maxArea2pointers(height)

    def maxArea2roop(self,height) -> int:
        ans = []
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                ans.append((j-i)*min(height[i],height[j]))
        print(ans,len(ans))
        return max(ans)

    def maxArea2pointers(self, height) -> int:
        left = 0
        right = len(height)-1
        m = 0
        while left < right:
            m = max(m,min(height[left],height[right])*(right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return m

testcases =[
    [1, 8, 6, 2, 5, 4, 8, 3, 7],
    [4, 3, 2, 1, 4],
    [1, 2, 1],
]
for height in testcases:
    sol = Solution().maxArea(height)
    print(sol)
