// old way:
function multiply(a, b) {
    var val1 = a || 1;
    var val2 = b || 1;
    console.log(val1 * val2);
}

multiply(3, 4);
multiply(4);
multiply(null, 3);
multiply();

// ES6 way:
const multiply2 = (c = 1, d = 1) => {
    console.log(c * d);
}

multiply2();
multiply2(3);
multiply2(4,5);