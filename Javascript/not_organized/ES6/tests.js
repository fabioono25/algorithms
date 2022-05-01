// working with template literal:
let one = 'One';
let two = 'Two';

console.log(`${one} - ${two}. \nHow are you?`);

// destructuring objects:
const personalInfo = {
    firstName: 'John',
    lastName: 'Nash',
    age: 23
};

const {firstName: fn, lastName: ln} = personalInfo;

//console.log(`${firstName} - ${lastName}.`);
console.log(`${fn} - ${ln}.`);

// destructuring arrays:
let names = ['Hal', 'Hen', 'Him'];
let [n1, n2, n3] = names;

n2 = 'Jane';
console.log(n1, n2, names[1]);

// object literal:
function test(firstName, lastName) {
    const newObj = {firstName, lastName};
    console.log(newObj);
}
test('James', 'Taylor');

// for of loop:
for (const name of names) {
    console.log(name);
}

// spread operator: 
console.log(...names); // values unwrapped

let x = [...names];
x = '';
console.log('names: ' + names); // the original array was not changed

// rest operator:
function restOperator(...names) {
    console.log(names);

    // reduce with arrow functions: 
    var total = names.reduce((x, y) => x + ' ' + y); 
    console.log(' after reduce: ', total);
}
restOperator(names);

// default parameters:
function sum(arr = []) {
    let total = 0;
    arr.forEach(element => {
        total += element;
    });
    console.log(total);
}
sum();
sum([1,2,3]);

// includes:
const numbers = [1,2,3];
console.log(numbers.includes(0)); // better than indexOf === -1

// import & export:
// import { data } from "./export";
// const x = data;
// x.push(11);
// console.log(x);

// padStart() and padEnd():
console.log('a'.padStart(10, 'b'));
console.log('a'.padEnd(10, 'b'));

// classes: 
class Animal {
    constructor(type) {
        this.type = type;
    }

    makeNoise(sound = 'bark') {
        console.log(sound);
    }

    static return10() {
        return 10;
    }

    get metaData() {
        return `${this.type}`;
    }
}

class Cat extends Animal {
    constructor(tail) {
        super('cat');
        this.tail = tail;
    }

    makeNoise(sound = 'meau') {
        console.log(sound);
    }
}

//import { Animal } from "./export"; - cannot use import outside a module - <script type="module" src="main.js"></script>
const dog = new Animal('dogui');
console.log(dog.metaData);

const cat = new Cat('asdasd');
cat.makeNoise();

// async and await:
const api = 'https://openweathermap.org/themes/openweathermap/assets/vendor/mosaic/data/wind-speed-new-data.json';

const fetch = require("node-fetch");

// using promises
function getResult() {
    fetch(api)
    .then(response => response.json())
    .then((json) => {
        console.log(json.en);
    })
    .catch((error) => {
        console.log(error);
    });
};

getResult();

async function getResultAsync() {
    const response = await fetch(api);
    const json = await response.json();

    console.log(json.en);
};

// function resolveAfter3Seconds() {
//     return new Promise(resolve => {
//         setTimeout(() => {
//             console.log('hi');
//         }, 3000);
//     });
// };

// resolveAfter3Seconds().then((data) => {
//     console.log('asdasdasd');
// });

// or 

// async function getAsyncData() {
//     const result = await resolveAfter3Seconds();
//     console.log(result);
// };

//getAsyncData();

// using Sets:
const example = new Set([1,1,1,2,3,4,4,4,4,4]);
example.add(5);
example.add('asd');
example.delete(2);
example.has(2);
console.log(example);