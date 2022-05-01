// using rest parameters
function fn(...args) {
    // using for..of to iterate over the elements
    // let total = 0;
    // for (const element of args) {
    //     total += element;
    // }
    // return total;

    return args
            .filter((e) => typeof e === 'number')
            .reduce((prev, cur) => prev + cur);
};

console.log(fn(1,2,'asd',3,4,5,6,7,'A'));

// using spread operators
const odd = [1,3,5];
const combined = [2, ...odd, 4, 6];
console.log(combined);