# We should design a queue abstract data type with the help of stacks, using a recursive approach
# methods: enqueue() dequeue() peek()

class Queue:
    def __init__(self):
        self.stack = []
    
    def enqueue(self, data):
        self.stack.append(data)

    # we are implicitly using the call-stack of the program (stack memory or execution stacks)
    def dequeue(self):
        if len(self.stack) == 0:
            raise Exception("Stacks are empty")

        if len(self.stack) == 1:
            return self.stack.pop()
        
        item = self.stack.pop()
        dequeued_item = self.dequeue()
        self.stack.append(item)

        return dequeued_item

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
