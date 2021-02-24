# inserting-items-into-an-array.py
class Solution:
    def duplicateZeros(self, arr) -> None:
        import queue
        q = queue.Queue()
        for i in arr:
            q.put(i)
            if i == 0:
                q.put(i)
        for i in range(len(arr)):
            arr[i] = q.get()

arr = [1,2,0,3,0,0,3,1,2,2]
Solution().duplicateZeros(arr)
