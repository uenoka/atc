# next-permutation.py
'''
ちょっといれ変えればいいかと思ったが意外と違った…
単調非減少でなくなる箇所（後ろから増減を見て初めて減少に転じる箇所）と増加箇所でちょうどその減少分の値を超えた個所を入れ替える
その後下の部分をreverse してあげればいい
単調非減少を探すのはO(1), 減少個所を丁度超える箇所を見つけるのは二分探索でO(logN)、入れ替えでO(1) , 逆順でO（N）
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        flg = False
        for i in reversed(range(1,len(nums))):
            if nums[i]>nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                flg = True
                break
        if not flg:
            nums = reversed(nums) 
        print(nums)

testcases = [
    [1,2,3,4,5],
    [1,3,2,45,56],
    [5,4,3,2,1],
    [1,1,2,2,2,2,2,3],
]
for nums in testcases:
    Solution().nextPermutation(nums)
