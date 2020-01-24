/**
 * https://dev.to/sethusenthil/var-vs-let-vs-const-1cgc
 * Hoisting is a JavaScript mechanism where variables and named function declarations are moved to the top
 *  of their scope before code execution. Inevitably, this means that no matter where functions 
 * and variables are declared, they are moved to the top of their scope regardless of whether their
 *  scope is global or local.
*/

(() => {
    console.log(i); //var i is undefined... this means the var is declared

    if (true) {
        var i = 100;
    }

    console.log(i); //var i has value 100, but it's out the if statement
})();


console.log(i); //now i is not defined - error

//the let statement use block similar to OOP or when 'use strict' in js.

(() => {
    console.log(i); //ReferenceError: i is not defined

    if (true) {
        let i = 100;
        console.log(i); //print 100
    }

    console.log(i); //ReferenceError: i is not defined
})();

//the Const just like let uses block scope, so it has all the properties of let besides the ability to prevent redeclaration of the variable. 

(() => {
    const message ="what up";
    console.log(message);
    message = "bye"; //Error: Message is already declared
    console.log(message);
})();

(() => {
    const message = {body:"what up", title:"rcs"};
    //Runkit is being weird please fix the obvious syntax error
    //If you know why this is happening please comment below!
    console.log(message);
    message.body = "bye";
    message.send = true;
    console.log(message);
    message = 100; //Error: message is already declared
    console.log(message);
})();