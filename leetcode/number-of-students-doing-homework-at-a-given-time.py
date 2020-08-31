# number-of-students-doing-homework-at-a-given-time.py
'''
なぜか同じコードで11%の速度だったり、94%だったりするから、同じオーダーだったらそんなに気にしなくてもよさそう。
'''


class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        cnt = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                cnt += 1
        return cnt


sol = Solution()
startTime = [1, 1, 1, 1]
endTime = [1, 3, 2, 4]
queryTime = 7
print(sol.busyStudent(startTime, endTime, queryTime))
