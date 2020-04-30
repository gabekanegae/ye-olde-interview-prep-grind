class MinStack:
    def __init__(self):
        self.content = []
        self.min = []

    def push(self, x):
        self.content.append(x)
        if self.min:
            self.min.append(x if x < self.min[-1] else self.min[-1])
        else:
            self.min.append(x)

    def pop(self):
        self.min.pop()
        return self.content.pop()

    def top(self):
        return self.content[-1]

    def getMin(self):
        return self.min[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top()) # return 0
print(minStack.getMin()) # return -2