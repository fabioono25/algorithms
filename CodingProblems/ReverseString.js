//create a function that reverses an input:
//Hi Fabio will be oibaF iH

function reverse(str) {

    //check
    if (!str || str.length < 2 || typeof str !== 'string')
    {
        return 'that is not good';
    }

    const invertedArray = [];

    for (let i = str.length-1; i >= 0; i--) {
        invertedArray.push(str[i]);
    }

    //return invertedArray.toString();
    return invertedArray.join('');
}

console.log(reverse('Hi Fabio'));

//built-in methods
function reverse2(str) {
    return str.split('').reverse().join('');
}

console.log(reverse2('Hi Fabio'));

//usig arrow functions
const reverse3 = str => str.split('').reverse().join('');

console.log(reverse3('Hi Fabio'));

//using spread operator
const reverse4 = str => [...str].reverse().join('');

console.log(reverse4('Hi Fabio'));
