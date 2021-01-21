# average-of-levels-in-binary-tree.py
'''
BSF, DSF 両方解法がきれいだと思ったので、両方で解きたい。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode):
        import queue
        q = queue.Queue()
        tmp = queue.Queue()
        ans = [root.val]
        q.put(root)
        while not q.empty():
            current = q.get()
            if current.left:
                tmp.put(current.left)
            if current.right:
                tmp.put(current.right)
            if q.empty():
                cnt = 0
                ave = 0
                while not tmp.empty():
                    tempnode = tmp.get()
                    q.put(tempnode)
                    ave += tempnode.val
                    cnt += 1
                if cnt != 0:
                    ans.append(ave/cnt)
        return ans
