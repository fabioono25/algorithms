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

// comparingArrays(['a','b','z'],['c','d']);
// comparingArrays(['a','b','z'],['c','a']);

//better solution
//we must consider divide the two loops in two different methods
//another thing to consider is verify the null values
//we must add better names for the variables and verify the size complexity (in this case is bigger)
function containsCommonItem(array1, array2){

    if (array1 == null || array2 == null){
        console.log('error');
        return false;
    }

    //loop first array and create properties === items in the array - O(n)
    let map = {};
    for (let i = 0; i < array1.length; i++) {
        const item = array1[i];
        map[item] = true;
    }

    //loop through second array and check if item in second array exists on created object - O(n)
    for (let j = 0; j < array2.length; j++) {
        if (map[array2[j]]) {
            console.log(true);
            return true;
        }
    }

    console.log(false);
} 
//O(a + b) - Time Complexity
//O(a) - Space Complexity

containsCommonItem(['a','b','z'],['c','d']);
containsCommonItem(['a','b','z'],['c','a']);
containsCommonItem(['a','b','z']);


//using specific language methods
function containsCommonItems2(array1, array2) {
    return array1.some(item => array2.includes(item));
}

console.log(containsCommonItems2(['a','b','z'],['c','d']));
console.log(containsCommonItems2(['a','b','z'],['c','a']));