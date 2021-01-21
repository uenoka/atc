# average-salary-excluding-the-minimum-and-maximum-salary.py
class Solution:
    def average(self, salary) -> float:
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)


sol = Solution()
salary = [8000, 9000, 2000, 3000, 6000, 1000]
print(sol.average(salary))
