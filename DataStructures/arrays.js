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
