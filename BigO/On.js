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

// What is the Big O of the below function? (Hint, you may want to go line by line)
function funChallenge(input) {
    let a = 10; //O(1)
    a = 50 + 3; //O(1)
  
    for (let i = 0; i < input.length; i++) { //O(n)
      anotherFunction();    //O(n)
      let stranger = true;  //O(n)
      a++; //O(n)
    }
    return a;  //O(1)
  }

  //result = BIG O(3 + 4n) -> O(n)
