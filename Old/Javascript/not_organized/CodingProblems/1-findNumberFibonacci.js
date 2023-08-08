//given a n, return the number in a Fibonacci series
//e.g. - What’s the number in n 6, in a Fibonacci series? R = 8. 


//Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21
//n          0  1  2  3  4  5  6   7  8
function findNumberFibonacci(n) {

    if (n < 0) return 0;

    if (n < 2) return n;

    let currentn = 2;
    
    let previousValue = 0;
    let lastValue = 1;

    while (currentn <= n) {
        const temp = lastValue;
        lastValue = lastValue + previousValue;
        previousValue = temp;
        currentn++;
    }

    return lastValue;
} //O(n)

//we can solve in a recursive way
function findNumberFibonacciRecursion(n) {
    if (n <= 0) {
        return 0
    } else if (n == 1) {
        return 1;
    } else {
        return findNumberFibonacciRecursion(n - 1) + findNumberFibonacciRecursion(n - 2);
    }
}

console.log(`n 0: ${findNumberFibonacci(0)}.`);
console.log(`n 1: ${findNumberFibonacci(1)}.`);
console.log(`n 2: ${findNumberFibonacci(2)}.`);
console.log(`n 3: ${findNumberFibonacci(3)}.`);
console.log(`n 4: ${findNumberFibonacci(4)}.`);
console.log(`n 5: ${findNumberFibonacci(5)}.`);
console.log(`n 6: ${findNumberFibonacci(6)}.`);
console.log(`n 7: ${findNumberFibonacci(7)}.`);
console.log(`n 8: ${findNumberFibonacci(8)}.`);
console.log(`n 40: ${findNumberFibonacci(40)}.`);
console.log(`n 80: ${findNumberFibonacci(80)}.`);

console.log(`n 8 with recursion: ${findNumberFibonacciRecursion(8)}.`);
console.log(`n 40 with recursion: ${findNumberFibonacciRecursion(40)}.`);