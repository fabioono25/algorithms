# We should design a queue abstract data type with the help of stacks
# methods: enqueue() dequeue() peek()

from collections import deque


class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []
    
    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty")

        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            
        return self.dequeue_stack.pop()

    def peek(self):
        return self.dequeue_stack[-1]

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(4)
    queue.enqueue(29)

    print(queue.dequeue())

    queue.enqueue(199)
    queue.enqueue(123)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
