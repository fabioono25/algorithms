const { performance } = require('perf_hooks');

//create a large array
// const largeArray = ['Dory','Nigel','Nemo','Marlin', 'Squirt'];

//FIRST RULE: we're looking for the WORST SCENARIO
//in Big O, we're looking for the worst scenario - Nemo at end
const largeArray = ['Dory','Nigel','Marlin', 'Squirt', 'Nemo']; 

//algorithm increases in linear mode O(n) -> Linear Time (fair)
function findNemo(array) {

    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'Nemo') {
            console.log(' found Nemo! ');
            break; //our code is more efficient
        }
    }
}

//findNemo(largeArray); //O(n) - worst scenario

//SECOND RULE: drop the constants = we don't care about n/2 or 100 

printFirstItemThenFirstHalfThenSayHi100Times(items) {
    console.log(items[0]); //O(1)

    var middleIndex = Math.floor(items.length / 2); //O(n/2) -> O(n)
    var index = 0;

    while (index < middleIndex) {
        console.log(items[index]);
        index++;
    }

    for (var i = 0; i < 100; i++) { //O(100) - O(1)
        console.log('hi');
    }
}

//result -> O(n + 1) = O(n)


//THIRD RULE: different terms for inputs
function compressBoxesTwice(boxes) {
    boxes.forEach(function(boxes){
        console.log(boxes);
    });

    boxes.forEach(function(boxes){
        console.log(boxes);
    });
}

//O(2n) -> O(n)

function compressBoxesTwice(boxes, boxes2) {
    boxes.forEach(function(boxes){  //O(a)
        console.log(boxes);
    });

    boxes2.forEach(function(boxes){ //O(b)
        console.log(boxes);
    });
} //different terms for inputs -> O(a + b)