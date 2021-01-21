# climbing-stairs.py
'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
N 段の階段があり、1-2 段上ることができる。
何パターンの上り方ができるか。
DP テーブルを「その段に来た時の上り方のパターン数」と考えて、N 段に来た時には、N-1, N-2 から到達できるので、その値を足してあげるという流れになる。
何となくN の累乗とかになりそうだから O(1) 解法もありそうかも。
→ よくよく考えたら An = An-1 + An-2 なのでフィボナッチ数と同じ。
'''


class Solution:

    def solve_memo(self, n: int) -> int:
        if n < 3:
            return self.memo[n]
        one_step = 0
        two_step = 0
        if self.memo[n-2] == 0:
            two_step = self.solve_memo(n-2)
            self.memo[n-2] = two_step
        else:
            two_step = self.memo[n-2]

        if self.memo[n-1] == 0:
            one_step = self.solve_memo(n-1)
            self.memo[n-1] = one_step
        else:
            one_step = self.memo[n-1]
        return one_step + two_step

    def solve_dp(self, n: int) -> int:
        for i in range(3, n+1):
            # print(self.dp)
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]

    def climbStairs(self, n: int) -> int:
        self.memo = [0]*(n+1)
        # self.memo[0] = 0
        # if n >= 1:
        #     self.memo[1] = 1
        # if n >= 2:
        #     self.memo[2] = 2
        # return self.solve_memo(n)
        self.dp = [0]*(n+1)
        self.dp[0] = 0
        if n >= 1:
            self.dp[1] = 1
        if n >= 2:
            self.dp[2] = 2
        return self.solve_dp(n)


sol = Solution()
n = 46
for i in range(1, n):
    # print(i)
    print(sol.climbStairs(i))
