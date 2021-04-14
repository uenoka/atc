#sum-of-all-odd-length-subarrays.py
class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        length = len(arr)
        i = 1
        ans = 0
        while i <= length:
            for j in range(length-i+1):
                ans += sum(arr[j:i+j])
            i+=2
        return ans

testcases =[
    [1, 4, 2, 5, 3],
    [1, 4],
    [10, 11, 12]
]
for arr in testcases:
    sol = Solution().sumOddLengthSubarrays(arr)
    print(sol)
