const { performance } = require('perf_hooks');

//create a large array
const largeArray = new Array(1000000).fill('asdasd');
largeArray.push('Nemo');

//algorithm running in constant time O(1) -> Constant time (excelent)
function logFirstTwoItems(array) {
    console.log(array[0]); //O(1)
    console.log(array[1]); //O(1)
}

logFirstTwoItems(largeArray); //O(1) - it doesn't matter how many returns will have in this case
//for convention it'll be always O(1)