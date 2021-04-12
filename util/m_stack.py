class m_stack():
    def __init__(self,size:int):
        self.idx = 0
        self.size = size
        self.stack_data = [0]*size
        print(self.stack_data)
    def push(self,val):
        if self.idx > self.size-1:
            print('full !!')
            return
        self.stack_data[self.idx] = val
        self.idx += 1

    def pop(self):
        self.idx -= 1
        if self.idx < 0:
            return "emmpty!"
        ret = self.stack_data[self.idx]
        return ret

    def getSize(self):
        return self.size

    def getCurrent(self):
        return self.idx

s = m_stack(5)
print('current is',s.getCurrent())
print('size is',s.getSize())
s.push(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(4)

print('current is',s.getCurrent())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())