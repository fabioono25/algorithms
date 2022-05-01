// a promise will finish in the future
const prom = new Promise((resolve, reject) => {
    // async operations
    setTimeout(() =>{
        //resolve(200);
        reject(new Error('something went wrong!'));
    }, 2000);
});

prom.then(data => {
    console.log(data);
})
.catch(err => console.log(err));
