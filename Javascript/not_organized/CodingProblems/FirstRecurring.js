//given an array = [2,5,1,2,3,5,1,2,4] - should return 2

//given an array = [2,1,1,3,4,5,6] - should return 1

//given an array = [2,3,4,5] - should return undefined

function firstRecurringCharacter(items) { //incomplete solution: [2,5,5,2,3]
    for (let i = 0; i < items.length; i++) {
        for (let j = i+1; j < items.length; j++) {
            if (items[i] === items[j]){
                return items[j];
            }
        }
        itemsToCompare.push(element);
    }
} //O(n^2)

firstRecurringCharacter([2,5,1,2,3,5,1,2,4])


function secondRecurringCharacter(items) {
    let itemsToCompare = [items[0]];

    for (let i = 1; i < items.length; i++) {
        const element = items[i];
        
        for (let j = itemsToCompare.length; j >= 0; j--) {
            if (element == itemsToCompare[j]){
                return itemsToCompare[j];
            }
        }
        itemsToCompare.push(element);
    }
} //O(n^2)

secondRecurringCharacter([2,5,1,2,3,5,1,2,4])

//now, using hashtables
function thirdRecurringCharacter(array) {
    let map = {}

    for (let i = 0; i < array.length; i++) {
        if (map[array[i]] != undefined) {
            return array[i];
        }
        else {
            map[array[i]] = i;
        }
        console.log(map)
    }
    return undefined;
} //O(n)

thirdRecurringCharacter([2,5,1,2,3,5,1,2,4])

//using set
function fourthRecurringCharacter(array) {
    let set = new Set();
    set.add(array[0]);
    
    for (let i = 1; i < array.length; i++) {
        if (set.has(array[i])){
            return array[i];
        }
        set.add(array[i]);
    }
    return undefined;
}

fourthRecurringCharacter([2,5,1,2,3,5,1,2,4])