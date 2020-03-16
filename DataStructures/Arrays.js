//Arrays are a collection of items organized sequentially

const strings = ['a','b','c','d']; //positions in memory 0, 1, 2, 3

//4 items - 32 bits -> 4 * 4 = 16 bytes of storage

//console.log(strings[2]);

strings[2]; //O(1)

//push
strings.push('e'); //O(1)

//pop
strings.pop(); //O(1)

console.log(strings);

//unshift (add in the beginning)
strings.unshift('x'); //O(n) - all items are reorganized in memory - not the best strategy to add items

//splice (add in the middle)
strings.splice(2, 0, 'z'); //O(n/2) => O(n)

console.log(strings);


//static arrays: C++
//int a[20]; int[5] {1, 2, 3, 4, 5} - to add one more item, we must copy the entire array

//in Javascript/Python, the arrays are automatically allocate memory according the increase resize
//with we add a new letter to initial strings array, it usually doubles the space (it'll copy the entire array)
