//Using Linked List

class Stack {
    constructor() {
        this.array = [];
    }

    peek() {
        return this.array[this.array.length-1];
    }

    push(value) {
        this.array.push(value);
        return this;
    }

    pop() {
        this.array.pop();
        return this;
    }
    //isEmpty
}

const myStack = new Stack();
myStack.push('A');
myStack.push('B');
myStack.push('C');
myStack.peek();
myStack.pop();
myStack.pop();
myStack.peek();