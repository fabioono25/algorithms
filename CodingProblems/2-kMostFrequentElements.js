//Find the K Most Frequent Elements for a given array

/**
 * Input: [1, 6, 2, 1, 6, 1, 6] K=2
 * Output: [1, 6]
 */

//array: elements, K=frequence
function frequenceElements(array, K) {

    //hashmap strategy with Linear Space & Time Complexity

    /**
     * frequency = {1: 3, 6: 3, 2:1}
     * bucket= [null, [2],[1,6], null]
     */

    let frequency = {};
    let bucket = [];
    let results = [];

    //here I the frequence hashmap and create the bucket
    array.forEach((val, i) => {
        if (frequency[val]) {
            frequency[val] += 1;
        }else {
            frequency[val] = 1;
            bucket[i+1] = null;
        }
    });

    //here I organize the items inside the bucket
    for (i in frequency){
        if (!bucket[frequency[i]]){
            bucket[frequency[i]] = [i];
        }else {
            bucket[frequency[i]].push(i);
        }
    }

    //now I should organize the output of some items
    for (let i = bucket.length; i > 0, results.length < K; i--) {
        if (bucket[i] != null) {
            results.push(...bucket[i]);
        }
    }

    return results;
}

console.log(frequenceElements([1, 6, 2, 1, 6, 1, 6], 2));