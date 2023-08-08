//Loop types in Javascript:
function findInArray(array) {
    for (let index = 0; index < array.length; index++) {
        console.log(array[i]);
    }
}

const findInArray2 = array => {
    array.forEach(item => {
        console.log(item);
    });
}

const findInArray3 = array => {
    for(let item of array) {
        console.log(item);
    }
}
