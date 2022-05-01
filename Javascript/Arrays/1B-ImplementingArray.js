class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
        return this.length;
    }

    pop() {
        const lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length--;
        return lastItem;
    }

    delete(index) {
      const item = this.data[index];
      this._shiftItems(index);
      return item;
    }

    _shiftItems(index) {
      for (let i = index; i < this.length; i++) {
        this.data[i] = this.data[i + 1];
      }
      delete this.data[this.length - 1]; // very last item treatment
      this.length--;
    }
}

const newArray = new MyArray();
//console.log(newArray.get(0));
newArray.push(1);
newArray.push(2);
newArray.push(3);
newArray.pop();
console.log(newArray.get(1));