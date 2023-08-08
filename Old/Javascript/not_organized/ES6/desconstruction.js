const list = {
    name: 'Name of the List',
    items: ['Item 1', 'Item 2']
}

const {name, items} = list;

console.log(name);
console.log(items);
console.log(...items);