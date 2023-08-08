class Product {
    constructor(name, value) {
        this.name = name;
        this.value = value;
    }
    printValue() {
        console.log(`The value for product ${this.name} is: ${this.value}.`);
    }
}

const myProduct = new Product('prod 1', 12.32);
myProduct.printValue();