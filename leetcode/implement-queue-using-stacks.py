# implement-queue-using-stacks.py
class MyQueue:

    def __init__(self):
        self.size = 10
        self.idx = 0
        self.head = 0
        self.queue = [0]*self.size

    def push(self, x: int) -> None:
        if self.head >= self.size:
            tmpQueue = [0]*self.size
            self.queue += tmpQueue
            self.size *= 2
        print(self.head,self.queue)
        self.queue[self.head] = x
        self.head += 1

    def pop(self) -> int:
        self.idx += 1
        return self.queue[self.idx - 1]

    def peek(self) -> int:
        return self.queue[self.idx]

    def empty(self) -> bool:
        return self.head == self.idx

