// given two arrays ([0,3,4,6], [4, 6, 7, 30]) merge them

function mergeSortedArrays(array1, array2) {
    const mergedArray = [];
    let array1Item = array1[0];
    let array2Item = array2[0];

    // extract these pieces of code into separate functions

    // check input
    if (array1.length === 0) {
        return array2;
    }

    if (array2.length === 0) {
        return array1;
    }

    // main procedure
    let i = 1, j = 1;
    while (array1Item || array2Item) {
        if (!array2Item || array1Item < array2Item) {
            mergedArray.push(array1Item);
            array1Item = array1[i];
            i++;
        } else {
            mergedArray.push(array2Item);
            array2Item = array2[j];
            j++;
        }
    }

    return mergedArray;
}


console.log(mergeSortedArrays([0,3,4,6], [4, 6, 7, 30]));