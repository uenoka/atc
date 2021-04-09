# valid-mountain-array.py
class Solution:
    def validMountainArray(self, arr) -> bool:
        mode = 'start'
        for i in range(1,len(arr)):
            # print('==',mode)
            if arr[i-1]==arr[i]:
                return False
            if mode == 'start':
                if arr[i-1] > arr[i]:
                    return False
                mode = 'climb'
            elif mode == 'climb':
                if arr[i-1] > arr[i]:
                    mode = 'down'
            elif mode == 'down':
                if arr[i-1] < arr[i]:
                    return False

        return mode == 'down'


testcases = [
    [1, 2, 3, 2, 1],
    [1, 3, 3, 2, 1],
    [3, 2, 1],
    [1, 2, 3],
]
for arr in testcases:
    sol = Solution().validMountainArray(arr)
    print(sol)
