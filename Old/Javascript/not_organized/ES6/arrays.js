const items = ['Item1', 'Item2', 'Item3'];

items.forEach((item, index) => {
    console.log(`Item:${item} - Index: ${index}.`);
});

const newList = items.map(item => `${item}-new`);
console.log(newList);

const filtered = items.filter(item => item === 'Item2');
console.log(filtered);

