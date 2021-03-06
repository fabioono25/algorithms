let user = {
    age: 54,
    name: 'John',
    magic: true,
    scream: () => {
        console.log('aaahhhhh!')
    }
}

console.log(user.age);      //O(1)

user.spell = 'asdasdasd';   //O(1)
user.scream(); //O(1)

//ES6: Map/Sets
const a = new Map(); //allows to save any datatype as the key (despite of string) - order of insertion maintained
const b = new Set(); //only stores the keys, no values


/*
create the methods set and get
*/
class HashTable {
    constructor(size){
      this.data = new Array(size); // how many spaces available
    }
  
    _hash(key) {
      let hash = 0;
      for (let i =0; i < key.length; i++){ //O(1)
          hash = (hash + key.charCodeAt(i) * i) % this.data.length
      }
      return hash;
    } //O(1) - using a key

    set(key, value){ // O(1)
        var address = this._hash(key);

        if (!this.data[address]){ // if a collision occurred
            this.data[address] = [];
        }
        
        this.data[address].push([key,value]);
    } //O(1)

    get(key){ // O(1) - considering no-collisions [can be O(n)]
        var address = this._hash(key);
        const currentBucket = this.data[address];

        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === address){
                    return currentBucket[i][1];
                }
            }
        } //O(1) - most of time

        return undefined;
    }

    //iterate through all the keys
    // keys() {
    //     const keysArray = [];
    //     for (let i = 0; i < this.data.length; i++) {
    //         if (this.data[i]) {
    //             keysArray.push(this.data[i][0][0])
    //         }           
    //     }
    //     return keysArray;
    // }

    keys() { //with collision prevention
        if (!this.data.length) {
          return undefined
        }
        let result = []
        // loop through all the elements
        for (let i = 0; i < this.data.length; i++) {
            // if it's not an empty memory cell
            if (this.data[i] && this.data[i].length) {
              // but also loop through all the potential collisions
              if (this.data.length > 1) {
                for (let j = 0; j < this.data[i].length; j++) {
                  result.push(this.data[i][j][0])
                }
              } else {
                result.push(this.data[i][0])
              } 
            }
        }
        return result; 
      }
  }

 
  const myHashTable = new HashTable(50);
  myHashTable.set('grapes', 10000)
  myHashTable.get('grapes')
  myHashTable.set('apples', 9)
  myHashTable.get('apples')
  myHashTable.keys();

  

