// Arrays 


// What are Generators in JavaScript?
// Generators in JavaScript are a special type of function that can be paused and resumed. 
// They are created using a function declaration. 
// When called, a generator function does not execute its code. 
// Instead, it returns a generator object that can be used to control the execution of the generator function.

// let x = [1, 'b', a => a+1 ]
// x.length = 5

// // for loop classic
// for (let i=0; i<x.length; i++){ // if it were for in or for of loop, we could have used const instead of let because it creates a new instance of the variable in each iteration.
//     console.log(`x: ${x[i]} of type ${typeof x[i]}`);
// }

// // for in loop 
// for (const i in x){ //* it skipes the undefined values
//     console.log(`x: ${x[i]} of type ${typeof x[i]}`);
// }   // returns x: 1 of type number, x: b of type string, x: a => a+1 of type function

// // for of loop
// for (const i of x){
//     console.log(`x ${i} of type ${typeof i}`);
// }

// let x = {'a': 1, b: 'b', 'c':[1,2,3]}

// for (const i in x ){
//     console.log(`keys: ${i}` )
//     console.log(`values: ${x[i]}` )
// }

// Objects are not iterable directly 
// Object.entries(x).map((key,value) => { // Objects.entries returns an array of key value pairs
//     console.log(`keys: ${key}` )
//     console.log(`values: ${value}` )    
// })

// Spread Operator 
// let x = [1,2,3]
// let y = [...x, 4, 5, 6] 
    

// let x = [1,2,3,4,5]

//! Javascript High Order Functions and Arrays:
// * forEach - calls a function for each element in an array
// * Does not return a new array; primarily used for side effects.

// x.forEach((item, index) => {
//     console.log(`${index} ---> ${item}`)
// })

// * map - calls a function for each element in an array
// * Returns a new array of the same length with the transformed elements.

// const doubledX = x.map((i, index) => {
//     return (i*2)
// })

// console.log(doubledX);

// * filter - filters elements in an array based on a provided function that returns a boolean.
// * Returns a new array with only the elements that pass the test.

// const filteredX = x.filter((i) => {
//     return i % 2 !== 0;
// })

// console.log(filteredX);

// * reduce - reduces an array to a single value based on a provided function.
// * Executes the function on each element of the array, passing the result to the next iteration.
// * reduce function takes in an accumulator and the current value.

// const items = [
//     {name: "book", price: 100},
//     {name: "pen", price: 30}, 
//     {name: "pencil", price: 10},
//     {name: "eraser", price: 20},
// ]

// const totalPrice = items.reduce((total,item) => {
//     // console.log(total);
//     return total + item.price
// }, 0)  // 0 is the initial value of the accumulator i.e. total

// console.log(totalPrice)

// * some - checks if at least one element in an array passes a test.
// * Returns a boolean value.

// const numbers = [1,2,3,4,5,6,7,8,9,10]
// const hasMultipleOfThree = numbers.some((i) => i % 3 === 0)
// console.log(hasMultipleOfThree);

// * every - checks if all elements in an array pass a test.
// * Returns a boolean value.

// const numbers = [1,2,3,4,5,6,7,8,9,10]
// const allArePositive = numbers.every((i) => i > 0)
// console.log(allArePositive);

// * find - returns the first element in an array that passes a test.
// * Returns the first element that satisfies the condition or undefined if no such element found.

// const numbers = [1,2,3,4,5,6,7,8,9,10]
// const isDivisibleBy4and8 = numbers.find(i => i%8 === 0 & i%4 === 0)
// console.log(isDivisibleBy4and8);

// * findIndex - returns the index of the first element in an array that passes a test.
// * Returns the index of the first element that satisfies the condition or -1 if no such element found.

// const numbers = [1,2,3,4,5,6,7,8,9,10]
// const firstMultipleOf5 = numbers.findIndex(i => i%5 === 0)
// console.log(numbers[firstMultipleOf5])


// spread operator used as remainder
// const [a, b, ...c] = [1,2,3,4,5,6,7,8,9]
// console.log(c)


// Node.js:
// Node.js is a runtime environment that allows you to run JavaScript code on the server side, outside of the browser. 
// It is built on the V8 JavaScript engine, which is the same engine that powers Google Chrome.
// Node.js allows developers to use JavaScript to write server-side code, build scalable network applications, do asynchronous I/O operations,
// and interact with the file system and other system-level functionalities.

// npm (Node Package Manager):
// npm is the default package manager for Node.js. It is used to install, manage, and share packages of reusable code.