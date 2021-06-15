//hi hello
//olleh ih

// basic solution
function reverse(str) {
    //check input
    if (!str || str.length < 2 || typeof str !== 'string') {
        return 'a problem occurred'
    }

    const backwards = [];
    for (let i=str.length-1; i >= 0; i--) {
        backwards.push(str[i]);
    }

    return backwards.join('');
}

// using functional approach
const reverse2 = str => str.split('').reverse().join('');

// using spread operator
const reverse3 = str => [...str].reverse().join('');

console.log(reverse('hi hello'));
console.log(reverse2('hi hello'));
console.log(reverse3('hi hello'));