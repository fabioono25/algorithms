//const basket = ['apples','grapes','pears'];

//linked list: apples(8947) -> grapes(8742) -> pears(372) -> null

//10 --> 5 --> 16

// let myLinkedList = {
//     head: {
//         value: 10,
//         next: {
//             value: 5,
//             next: {
//                 value: 16, //tail
//                 next: null
//             }
//         }
//     }
// }

class Node { //it's possible to use this class
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }

        this.tail = this.head; //because we have only one object for now
        this.length = 1;
    }

    append(value) {
        const newNode = {
            value: value,
            next: null
        }

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
            next: this.head
        }

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

        // if (index === 0) {
        //     this.prepend(value);
        //     return this.printList();
        // }

        if (index >= this.length) {
            return this.append(value);
        }

        const newNode = new Node(value);

        let leader = this.traverseToIndex(index-1);
        const holdingPointer = leader.next;

        leader.next = newNode;
        newNode.next = holdingPointer;
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
}


const myLinkedList = new LinkedList(10);

myLinkedList.append(5);
myLinkedList.append(16);

myLinkedList.prepend(1);
//console.log(myLinkedList.printList());

myLinkedList.insert(2, 99); //1 --> 10 --> 99 -- > 5 --> 16

//myLinkedList.insert(222, 102); //1 --> 10 --> 99 -- > 5 --> 16

console.log(myLinkedList.printList());
