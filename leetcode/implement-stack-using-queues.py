
class MyStack:
    def __init__(self):
        self.size = 100
        self.stack = [0]*self.size
        self.idx = 0

    def push(self, x: int) -> None:
        if self.idx >= self.size:
            tmpStack = [0]*self.size
            self.stack += tmpStack
            self.size *= 2
        self.stack[self.idx] = x
        self.idx += 1

    def pop(self) -> int:
        self.idx -= 1
        return self.stack[self.idx]

    def top(self) -> int:
        return self.stack[self.idx - 1]

    def empty(self) -> bool:
        return self.idx == 0
