let largeArray = new Array(10000).fill('nemo');

function findNemo(arr) {
    // const t0 = performance.now();
    const t0 = Date.now();
    for (let index = 0; index < arr.length; index++) {
        if (arr[index] === 'nemo'){
            console.log('found nemo!');
        }
    }
    // const t1 = performance.now();
    const t1 = Date.now();
    console.log(`performance: ${t1-t0}.`)
};

function logFirstItems(arr) {
    console.log(arr[0]); // O(1)
    console.log(arr[1]); // O(1)
}

findNemo(largeArray); // O(n): Linear Time to find Nemo
logFirstItems(largeArray); // O(2) operations -> O(1)
