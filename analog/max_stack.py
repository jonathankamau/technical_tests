class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = [0]

    def push(self,val):
        if val > self.max_stack[-1]:
            self.max_stack.append(val)
        self.stack.append(val)
    
    def pop(self):
        popped_value = self.stack.pop()
        if popped_value == self.max_stack[-1]:
            self.max_stack.pop()
    
    def max(self):
        return self.max_stack[-1] or None
# Test Cases
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
