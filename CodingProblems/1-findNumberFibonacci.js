//given a position, return the number in a Fibonacci series
//e.g. - What’s the number in position 6, in a Fibonacci series? R = 8. 


//Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21
//position          0  1  2  3  4  5  6   7  8
function findNumberFibonacci(position) {

    if (position < 2) return position;

    let currentPosition = 2;
    
    let previousValue = 0;
    let lastValue = 1;

    while (currentPosition <= position) {
        const temp = lastValue;
        lastValue = lastValue + previousValue;
        previousValue = temp;
        currentPosition++;
    }

    return lastValue;
} //O(n)

console.log(`Position 0: ${findNumberFibonacci(0)}.`);
console.log(`Position 1: ${findNumberFibonacci(1)}.`);
console.log(`Position 2: ${findNumberFibonacci(2)}.`);
console.log(`Position 3: ${findNumberFibonacci(3)}.`);
console.log(`Position 4: ${findNumberFibonacci(4)}.`);
console.log(`Position 5: ${findNumberFibonacci(5)}.`);
console.log(`Position 6: ${findNumberFibonacci(6)}.`);
console.log(`Position 7: ${findNumberFibonacci(7)}.`);
console.log(`Position 8: ${findNumberFibonacci(8)}.`);
console.log(`Position 40: ${findNumberFibonacci(40)}.`);
console.log(`Position 80: ${findNumberFibonacci(80)}.`);