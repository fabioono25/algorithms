//Implement a queue using stacks

//Queue: FIFO
//Stack: LIFO
//first we can create a stack implementation
class Stack {
    constructor() {
        this.array = [];
    }

    push(value) {
        this.array.push(value);
    }

    pop() {
        return this.array.pop();
    }

    peek() {
        return this.array[this.array.length-1];
    }

    isEmpty() {
        return this.array.length === 0;
    }
}

class QueueUsingStack {
    constructor() {
        this.pushStack = new Stack();
        this.popStack = new Stack();
    }

    enqueue(value) {
        this.pushStack.push(value);
    }

    peek() {
        if (this.popStack.isEmpty()) {
            this.moveInStacks();
        }
        return this.popStack.peek();
    }

    dequeue() {
       if (this.popStack.isEmpty()) {
           this.moveInStacks();
       }
       
       return this.popStack.pop();
    }

    moveInStacks() {
        while(!this.pushStack.isEmpty())
            this.popStack.push(this.pushStack.pop()); //O(n) - max
    }
}

let queue = new QueueUsingStack();
queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.dequeue();   //10
queue.enqueue(50);
queue.enqueue(60);
queue.dequeue();   //20
queue.dequeue();   //30
queue.dequeue();   //40
queue.dequeue();   //50
queue.dequeue();   //60 
queue.dequeue();   //undefined

