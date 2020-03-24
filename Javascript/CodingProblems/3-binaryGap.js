//Find longest sequence of zeros in binary representation of an integer (0 if no binary gap found).

/**
 * 9 has a binary representation of 1001 (binary gap of two)
 * 529 has a binary representation of 1000010001 and two binary gaps (the biggest one with four)
 * 32 has a binary representation of 100000 and 0 binary gaps
 */

function findBinaryGap(number) {

    //first, we must convert the number into binary value
    const binaryValue = (number >>> 0).toString(2);

    //now, we shoud iterate between these values to count the gaps

    let totalCount = 0;
    gapCount(binaryValue);

    function gapCount(number) {

        const firstIndex = number.indexOf(1)+1;
        const secondIndex = number.indexOf(1, number.indexOf(1) + 1);

        if (firstIndex === -1 || secondIndex == -1)
            return;

        count = number.substring(firstIndex, secondIndex).length;

        if (count > totalCount)
            totalCount = count;

        if (number.indexOf(1, secondIndex + 1) != -1) {
            gapCount(number.slice(secondIndex));
        }
    }

    return totalCount;
}

console.log(findBinaryGap(9));
console.log(findBinaryGap(529));
console.log(findBinaryGap(32));
