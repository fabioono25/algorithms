//Move all zeroes present in the array to the end and return the same array 

/**
 * Input: [1, 0, 0, 2, 0, 3, 0, 0] or [0, 0, 1, 2, 0, 3, 0, 0]
 * Output: [1, 2, 3, 3, 0, 0, 0, 0]
 */

function zeroRepositioning(arr) {

    let zeroIndex = -1;

    for (let i = 0; i < arr.length; i++) { //O(n)
        if (arr[i] === 0) {
            if (zeroIndex === -1) {
                zeroIndex = i;
            }
        } else {
            if (zeroIndex !== -1 && i !== zeroIndex){
                arr[zeroIndex] = arr[i];
                zeroIndex += 1;
            }
        }
    }

    if (zeroIndex !== -1)
        for (let i = zeroIndex; i < arr.length; i++) { //O(n)
            arr[i] = 0;
        }
    
    return arr;
} //O(n)


console.log(zeroRepositioning([1, 0, 0, 2, 0, 3, 0, 0]));
console.log(zeroRepositioning([0, 0, 1, 2, 0, 3, 0, 0]));