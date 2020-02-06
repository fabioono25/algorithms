const a = 1; //we just allocate memory (Memory Heap)
const b = 2;
const c = 100;

//call stack
console.log('1');
console.log('2');
console.log('3');

//calls stack -> two()one()
const one = () => {
    const two = () => {
        console.log('4');
    }
    two();
}

//Javascript is a single threaded language that can be non-blocking. 
//one call stack (LIFO)
//multithreading can cause deadlocks

//stack overflow - recursion
function foo() {
    foo()
}

foo();

//asynchronous simulation
console.log('1');

setTimeout(() => {
    console.log('2');
})

console.log('3');

//call stack

//web api

//callback queue

//event loop

