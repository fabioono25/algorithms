# We have a stack and we want to track the largest item during instertion
# getMax() method should have O(1) running time complexity. We can have O(N) space complexity.

class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
    
    def push(self, data):
        self.main_stack.append(data)

        if (len(self.main_stack) == 1):
            self.max_stack.append(data)
            return

        if (data > self.max_stack[-1]):
            self.max_stack.append(data)
        
    def pop(self):
        data = self.main_stack[-1]
        self.main_stack.pop()
        return data

    def get_max_item(self):
        return self.max_stack[-1]

if __name__ == '__main__':
    max_stack = MaxStack()

    max_stack.push(100)
    max_stack.push(10)
    max_stack.push(0)
    max_stack.push(10)
    max_stack.push(1)
    max_stack.push(1020)
    max_stack.push(1230)
    max_stack.push(0)

    print(max_stack.get_max_item())
