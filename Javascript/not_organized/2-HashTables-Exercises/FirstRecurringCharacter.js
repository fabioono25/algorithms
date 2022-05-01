// [2,5,1,2,3,4,1,2,4] - 2
// [2,1,1,2,3,5,6,5] - 1
// [1,3,5] - undefined

//super-naive approach [time complexity of O(n^2)], space complexity of O(1)
function firstRecurringCharacter(input) {
    for (let i = 0; i < input.length; i++) {
        const element = input[i];
        for (let j = i+1; j < input.length; j++) {
            const nextElement = input[j];
            if (element === nextElement) {
                return element;
            }
        }
    }
}

// now, using a HashTable
function firstRecurringCharacterV2(input) {
    let map = {}; // keys will be unique - the space complexity was increased by O(n) - new structure
    for (let i = 0; i < input.length; i++) {
        if (map[input[i]] !== undefined) { // the key already exists
            return input[i];
        } else {
            map[input[i]] = i;
        }
    }
} // O(n)

console.log(firstRecurringCharacter([2,5,1,2,3,4,1,2,4]));
console.log(firstRecurringCharacter([2,1,1,2,3,5,6,5] ));
console.log(firstRecurringCharacter([2,1,4]));

console.log(firstRecurringCharacterV2([2,5,1,2,3,4,1,2,4]));
console.log(firstRecurringCharacterV2([2,1,1,2,3,5,6,5] ));
console.log(firstRecurringCharacterV2([2,1,4]));