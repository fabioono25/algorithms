//given two arrays, you must merge them in order

//mergeSortedArrays([0,3,4,31],[4,6,30]); // [0,3,4,6,30,31]


function mergeSortedArrays(arr1, arr2) {

    const mergedArray = [];
    let array1Item = arr1[0];
    let array2Item = arr2[0];
    let i = 1;
    let j = 1;

    //check inputs
    if (arr1.length === 0) {
        return arr2;
    }

    if (arr2.length === 0) {
        return arr1;
    }

    while (array1Item || array2Item) {
        console.log(array1Item, array2Item);
        if (!array2Item || array1Item < array2Item) {
            mergedArray.push(array1Item);
            array1Item = arr1[i];
            i++;
        } else {
            mergedArray.push(array2Item);
            array2Item = arr2[j];
            j++;
        }
    }

    return mergedArray;
}

console.log(mergeSortedArrays([0,3,4,31],[4,6,30]));


//using built-in functions
function mergeSortedArrays2(arr1, arr2) {

    //add arr2 into arr1
    arr1.push(...arr2);
    
    //sort array
    arr1.sort((a, b ) => a - b);
    
    return arr1.filter((item, pos, ary) => {
        return item != ary[pos - 1];
    });
}

console.log(mergeSortedArrays2([0,6,4,31],[4,3,30]))
