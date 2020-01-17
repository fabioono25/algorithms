//log all pairs of array
const boxes = ['a','b','c','d','e'];

//the Big O notation = O(n * n) -> O(n^2)  - Alt+94
function logAllPairsOfArray(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            console.log(array[i], array[j]);            
        }
    }
}

logAllPairsOfArray(boxes);