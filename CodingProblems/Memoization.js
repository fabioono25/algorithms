function addTo80() {
    return n + 80;
}

addTo80();
addTo80(); //no cache

let cache = {
    //5: 85
};

function memorizedAddTo80(n) {
    if (n in cache) { //cache.n
        return cache.n; //cache[n]
    } else {
        cache[n] = n + 80;
        return cache[n];
    }
}

memorizedAddTo80(5);
memorizedAddTo80(5); //get from cache

// let's make that better with no global scope. This is closure in javascript so.
function memoizeAddTo80(n) { 
    let cache = {};
    return function(n) {
      if (n in cache) {
        return cache[n];
      } else {
        console.log('long time');
        const answer = n + 80;
        cache[n] = answer;
        return answer;
      }
    }  
  }

  const memoized = memoizeAddTo80();
  console.log(1, memoized(6))
  // console.log(cache)
  // console.log('-----------')
  console.log(2, memoized(6))
  