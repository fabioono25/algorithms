/**
 * Write two functions that finds the factorial of any number. 
 * One should use recursive, the other should just use a for loop
 **/

function findFactorialRecursive(number) {
    
    // if (number === 2) {
    //     return 2;
    // }

    // if (number === 1) {
    //     return 1;
    // }

    if (number <= 2) {
        return number;
    }

    answer = number * findFactorialRecursive(number - 1);

    return answer;
  } //time complexity = O(n)
  
  function findFactorialIterative(number) {
    
    let answer = 1;

    if (number === 2) {
        answer = 2;
    }

    for (let i = 2; i <= number; i++) {
        answer = answer * i;
    }

    return answer;
  } //Time complexity = O(n)
  