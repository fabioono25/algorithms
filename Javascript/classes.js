//reference type:

var number1 = 1; //primitive types, like true, "hi", undefined, null, true
var number2 = 1;

console.log(number1 === number2); //true

var obj1 = { value: 10 }
var obj2 = { value: 10 }

console.log(obj1 === obj2); //false

var obj3 = obj1;

console.log(obj1 === obj3); //true

var arr1 = [];
var arr2 = [];

console.log(arr1 === arr2); //false

//context vs scope
function test() { //new scope
    let a = 4;
}

//context: where we are within the object
console.log(this);

const object4 = {
    a: function() {
        console.log(this)
    }
}

console.log(a);

//instantiation: you make a copy of the object to use it
//ES6
class Player {
    constructor(name, type) {
        console.log(`Player: ${this}.`);
        this.name = name;
        this.type = type;
    }

    introduce() {
        console.log(`hi I am ${this.name}. I'm a ${this.type}.`)
    }
}

class Wizard extends Player {
    constructor(name, type) {
        super(name, type)
        console.log(`Wizard: ${this}.`);
    }
    play() {
        console.log(`I'm a ${this.type}.`)
    }
}

const wizard1 = new Wizard('Shelly', 'Healer');
const wizard2 = new Wizard('Shaw', 'Dark Magic');

//classical inheritance approach (before ES6):
var Player = function(name, type){
    this.name = name;
    this.type = type;
}

Player.prototype.introduce = function() {
    console.log(`hi I am ${this.name}. I'm a ${this.type}.`)
}

const wizard1 = new Player('Shelly', 'Healer');
const wizard2 = new Player('Shaw', 'Dark Magic');

wizard1.play = function() {
    console.log(`I'm a ${this.type}.`)
}

wizard2.play = function() {
    console.log(`I'm a ${this.type}.`)
}