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

findNemo(largeArray); //O(n) - worst scenario