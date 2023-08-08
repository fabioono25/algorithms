// Given a number N return the index value of the Fibonacci sequence, where the sequence is:

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
// the pattern of the sequence is that each value is the sum of the 2 previous values, 
// that means that for N=5 → 2+3

//For example: fibonacciRecursive(6) should return 8

function fibonacciIterative(n){ //O(n)
    let arr = [0,1];

    for (let i = 0; i < n + 1; i++) {
        arr.push(arr[i-2] + arr[i-1])
    };

    return arr[n];
}

fibonacciIterative(3);
  
function fibonacciRecursive(n) { //O(2^n) - a lot of calculations - not efficient

    if (n < 2) {
        return n;
    }

    return findFactorialRecursive(n-1) + fibonacciRecursive(n-2);
}

fibonacciRecursive(3)

//using dynamic programming to solve Fibonacci: O(n)
function fibonacciWithCache() {
    let cache = {};
    return function fib(n) { //time complexity: O(n) -- drawback is space complexity
        if (n in cache) {
            return cache[n];
        } else 
        {
            if (n < 2) {
                return n;
            }
            else {
                cache[n] = fib(n-1) + fib(n-2);
                return cache[n];
            }
        }
    }
}

const fasterFib = fibonacciWithCache();
fasterFib(10);

//dynamic 2:
function fiboDynamicV2(n){ //bottom-up approach
    let answer = [0, 1];
    for (let i = 2; i < n; i++) {
        answer.push(answer[i-2] + answer[i-1]);
    }
    return answer.pop();
}

