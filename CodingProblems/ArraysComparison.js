//given 2 arrays, create a function that let's a user know where two arrays contain any common items

// const array1 = ['a', 'b'];
// const array2 = ['c', 'd'];
// shoud return false

// const array1 = ['a', 'b'];
// const array2 = ['c', 'a'];
// should return true


//what's more important? time complex | space complex?
//performance
function comparingArrays(array1, array2) { //O(n^2)

    // for (const key in array1) {
    //     console.log(key);
    // }
    
    //O(a*b) -> O(n^2) - arrays from different sizes
    for (let i=0; i<array1.length; i++) {
        for (let j=0; j<array1.length; j++) {
        
            if (array1[i] === array2[j]){
                console.log('true');
                return true;
            }
        }    
    }
    console.log('false');
    return false;

    //trying something faster using Hashtables - common pattern
    //array1 => object {a:true, b:true, c:true, x:true}
}

function containsCommonItem(array1, array2){
    //loop first array and create properties === items in the array - O(n)


    //loop through second array and check if item in second array exists on created object - O(n)


} //O(a + b)


comparingArrays(['a','b','z'],['c','d']);
comparingArrays(['a','b','z'],['c','a']);

