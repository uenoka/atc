# min-stack.py
'''
push, pop で毎回最小値かどうか比較しないといけない
pop した値が最小なら2番目に小さい値を最小値に設定しないといけない → 優先度付きキューで管理する
heapq の使い方とかはあまりうまくできなかったり、実装速度が遅かったりするけど、これくらいならまぁできるよねという感じにはなってきた。
後で two stacks の解法も見てみる。
'''
import heapq as hq
class MinStack:
    def __init__(self):
        self.stack = []
        self.minVal = []
        hq.heapify(self.minVal)

    def push(self, val: int) -> None:
        self.stack.append(val)
        hq.heappush(self.minVal,val)

    def pop(self) -> None:
        current = self.stack.pop()
        self.minVal.remove(current)
        hq.heapify(self.minVal)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[0]


tmp = [0,1,3,4,5,6]
print(tmp.pop())
print(tmp)
print(tmp.pop(6))
print(tmp)
