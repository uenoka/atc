# robot-return-to-origin.py
'''
普通にカウントしていく解法
'''


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        side_cnt = 0
        up_cnt = 0
        for c in moves:
            if c == 'U':
                up_cnt += 1
            if c == 'D':
                up_cnt -= 1
            if c == 'L':
                side_cnt += 1
            if c == 'R':
                side_cnt -= 1
        return side_cnt == 0 and up_cnt == 0

    '''
    counter 使ってみる解法
    こっちのほうが早め。（単純にsetにしているわけじゃなくて個数管理してるからO(N)かかりそうな気もするけど。）
    '''

    def judgeCircle2(self, moves: str) -> bool:
        import collections
        L = list(moves)
        C = collections.Counter(L)
        return C["U"] == C["D"] and C["R"] == C["L"]


sol = Solution()
moves = 'UUDDLR'
print(sol.judgeCircle2(moves))
