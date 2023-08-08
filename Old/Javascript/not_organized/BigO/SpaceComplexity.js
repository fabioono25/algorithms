function booo(n) {
    for (let i = 0; i < n.length; i++) {
        console.log('boo!');
    }
}

booo([1,2,3,4,5]); //Space complexity of O(1) - just adding variable i in for

function arrayOfNTimes(n) {
    let hiArray = [];

    for (let i = 0; i < n; i++) {
        hiArray[i] = 'hi!';
    }

    return hiArray;
}

arrayOfNTimes(6); //O(n) - we're generating new variable position in memory for iteration

