class m_queue():
    def __init__(self, size):
        self.size = size
        self.data = [0]*size
        self.tail_idx = 0
        self.head_idx = 0
    def enqueue(self,val):
        if self.tail_idx >= self.size:
            print("full !!")
            return
        self.data[self.tail_idx] = val
        self.tail_idx += 1
    def dequeue(self):
        if self.head_idx >= self.size or self.head_idx == self.tail_idx:
            return "empty"
        ret = self.data[self.head_idx]
        self.head_idx += 1
        return ret
queue = m_queue(5)
print(queue.size)
print(queue.head_idx)
print(queue.tail_idx)
print('---')
queue.enqueue(0)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(1)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
