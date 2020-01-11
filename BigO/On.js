const { performance } = require('perf_hooks');

//create a large array
const largeArray = new Array(1000000).fill('asdasd');
largeArray.push('Nemo');

//algorithm increases in linear mode O(n) -> Linear Time (fair)
function findNemo(array) {

    //let t0 = performance.now();
    // for (let i = 0; i < array.length; i++) {
    //     if (array[i] === 'Nemo') {
    //         console.log(' found Nemo! ');
    //     }
    // }

    largeArray.forEach((item) => {
        if (item === 'Nemo') {
            console.log(' found Nemo!');
        }
    })

    // let t1 = performance.now();
    // console.log(`Time to find Nemo: ${t1 - t0}`);
}

findNemo(largeArray);