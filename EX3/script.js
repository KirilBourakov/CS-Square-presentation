console.log('Hello, world')

// creating a function, and assigning it to a var
function add1(inp) {
    return inp + 1
}
let add1var = add1
console.log('Calling add1:', add1(1))
console.log('calling add1var:', add1var(1))

// creating a function
let add2WithLoop = (inp) => {
    for(let i = 0; i < 2; i++){
        inp++;
    }
    return inp
}

console.log('calling add2WithLoop:', add2WithLoop(1))

// equality
console.log("'2' == 2:", '2' == 2)
console.log("'2' === 2:", '2' === 2)

// you can declare objects with just curly braces
let obj = {a: 1, b: 2, c: 3, func: add2WithLoop}
console.log(obj)