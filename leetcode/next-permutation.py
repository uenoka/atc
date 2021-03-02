# next-permutation.py
'''
ちょっといれ変えればいいかと思ったが意外と違った…
単調非減少でなくなる箇所（後ろから増減を見て初めて減少に転じる箇所）と増加箇所でちょうどその減少分の値を超えた個所を入れ替える
その後下の部分をreverse してあげればいい
単調非減少を探すのはO(N), 減少個所を丁度超える箇所を見つけるのは二分探索でO(logN)、入れ替えでO(1) , 逆順でO（N）なので全体としてはO(N)で解くことができる。
ごみのようにこういう添え字系苦手だな…頭の中でこういうのが考えられて実装も詰まらずできるようになりたい…
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        i = len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i -= 1
        if i==0 : 
            nums.reverse()
            return
        targetIdx = i-1
        j = len(nums)-1
        while j>0 and nums[targetIdx] >= nums[j]:
            j-=1
        swapIdx = j
        print(targetIdx,swapIdx)
        print('bef',nums)
        nums[targetIdx], nums[swapIdx] = nums[swapIdx], nums[targetIdx]
        print('aft',nums)
        end = len(nums)-1
        targetIdx+=1
        while end > targetIdx:
            nums[targetIdx], nums[end] = nums[end], nums[targetIdx]
            targetIdx+=1
            end-=1
        print(nums)

testcases = [
    [1,1,4,5,4,3,2,1], 
    [1, 3, 2],
    [4,3,2,1],
    [1, 1],
    [5, 1, 1]
]
for nums in testcases:
    Solution().nextPermutation(nums)
