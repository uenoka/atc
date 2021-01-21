# replace-elements-with-greatest-element-on-right-side.py
'''
O(N^2) 解法。Runtime も4秒程度。
O(N) 解法があるっぽい。
→逆順にしたら最大値を保存しておきながら進めることができる。
'''
class Solution:
    def replaceElements(self, arr):
        ans = [0]*len(arr)
        ans[-1]=-1
        for i in range(len(arr)-1):
            ans[i]= max(arr[i+1:])
        return ans

    def replaceElements2(self, arr):
        length = len(arr)-2
        ans = [-1]*len(arr)
        currentMax = arr[-1]
        while length>=0:
            currentMax = max(currentMax,arr[length+1])
            ans[length] = currentMax
            length -= 1
        return ans


sol = Solution()
arr = [17,18,5,4,6,1]
print(sol.replaceElements2(arr))