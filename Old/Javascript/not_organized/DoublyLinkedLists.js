class Node { //it's possible to use this class
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
            prev: null
        }

        this.tail = this.head; //because we have only one object for now
        this.length = 1;
    }

    append(value) {
        const newNode = {
            value: value,
            next: null,
            prev: null
        }

        newNode.prev = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;

        return this;
    }

    //10 --> 5 --> 16
    //1 --> 10 --> 5 --> 16
    prepend(value) {
        const newNode = {
            value: value,
            next: this.head,
            prev: null
        }

        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode;
        this.length++;

        return this;
    }

    printList() {
        const array = [];
        let currentNode = this.head;

        while(currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }

        //console.log(array);
        return array;
    }

    insert(index, value) {
        if (index >= this.length) {
            return this.append(value);
        }

        const newNode = new Node(value);

        let leader = this.traverseToIndex(index-1);
        const follower = leader.next;

        leader.next = newNode;
        newNode.prev = leader;
        newNode.next = follower;
        follower.prev = newNode;
        this.length++;

        return this.printList();
    }

    traverseToIndex(index) {
        let counter = 0;
        let currentNode = this.head;

        while(counter !== index){
            currentNode = currentNode.next;
            counter++;
        }

        return currentNode;
    }

    remove(index) {
        //check the parameters
        const leader = this.traverseToIndex(index-1); //O(n)
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;

        this.length--;
        return this.printList();
    }
}


const myLinkedList = new DoublyLinkedList(10);

myLinkedList.append(5);
myLinkedList.append(16);

myLinkedList.prepend(1);
//console.log(myLinkedList.printList());

myLinkedList.insert(2, 99); //1 --> 10 --> 99 -- > 5 --> 16

//myLinkedList.insert(222, 102); //1 --> 10 --> 99 -- > 5 --> 16

//myLinkedList.remove(3); //[ 1, 10, 99, 16 ]

console.log(myLinkedList);

console.log(myLinkedList.printList());
