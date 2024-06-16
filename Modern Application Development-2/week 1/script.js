// document.addEventListener('DOMContentLoaded', (event) => {
//     console.log('Document is fully loaded');
    
//     const heading = document.querySelector('h1');
//     heading.addEventListener('click', () => {
//         alert('You clicked the heading!');
//     });
// });

// const v = [1,2,3,4]
// // for in 
// for (const x in v){
//     console.log(x);
// }
// // for of
// for (const x of v){
//     console.log(x);
// }

// * Assignment Week 1
/*
 * calculateSimpleInterest calculates and returns the simple interest
 * (floor value) for a fixed deposit. Formula used is,

 * calculateSimpleInterest calculates and returns the simple interest
 * for a fixed deposit. Formula used is,
 * Simple Interest: P X R X T / 100
 *   where:
 *   P = Principal
 *   I = Daily interest rate
 *   N = Number of days
 *
 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - daily interest rate
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} interest
*/

/*
 * calculateCompoundInterest calculates and returns the compound interest
 * (floor value) for a fixed deposit. Formula used is,
 *   Compound Interest=P[(1+I/100)^N - 1]
 *   where:
 *   P = Principal
 *   I = Daily interest rate
 *   N = Number of days
 *
 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - daily interest rate
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} interest
*/

/*
 * extraAmountPercentage calculates and returns the extra amount percentage borrower will have to pay in case of
 * compound interest (floor value) in comparison to the simple interest for a fixed deposit.

 *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
 *
 * @param {number} principal  - Principal amount
 * @param {number} dailyInterest  - Daily interest rate.
 * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
 * @return {number} percentage
*/

function calculateSimpleInterest(
    principal,
    dailyInterest,
    startingDate,
    endingDate
  ) {
    
    //TODO: add type checks for all the inputs
    if (isNaN(principal) || isNaN(dailyInterest)){
        return -1 
    }

    const yes = new Date(startingDate);
    const tod = new Date(endingDate);

    if (isNaN(yes.getTime()) || isNaN(tod.getTime())){
        return -1 
    }

    const diff = tod - yes;
    const diffDays = diff/ (1000*60*60*24)
  
    const interest = (principal*dailyInterest*diffDays) / 100;
  
    return Math.floor(interest);
  
  }

// console.log(calculateSimpleInterest(20000, 1, "2020-12-27", "2021-08-27"))



function calculateCompoundInterest(
principal,
dailyInterest,
startingDate,
endingDate
) {
    if (isNaN(principal) || isNaN(dailyInterest)){
        return -1 
    }

    const yes = new Date(startingDate);
    const tod = new Date(endingDate);

    if (isNaN(yes.getTime()) || isNaN(tod.getTime())){
        return -1 
    }
    const diff = tod - yes;
    const diffDays = diff/ (1000*60*60*24)
    // console.log('diffDays',diffDays);

    const subInterest = 1 + (dailyInterest/100)
    // console.log("subInterest",subInterest);

    const subInterestPower = subInterest ** diffDays
    // console.log("subInterestPower", subInterestPower)

    const interest = principal*(subInterestPower - 1)
    // console.log('interest',interest)

  return Math.floor(interest);

}

console.log(calculateCompoundInterest(20000,1,"2020-12-27","2021-08-27"))
  
function extraAmountPercentage(
principal,
dailyInterest,
startingDate,
endingDate
) {
    if (isNaN(principal) || isNaN(dailyInterest)){
        return -1 
    }

    const yes = new Date(startingDate);
    const tod = new Date(endingDate);

    if (isNaN(yes.getTime()) || isNaN(tod.getTime())){
        return -1 
    }

    const simpleInterest = calculateSimpleInterest(principal, dailyInterest, startingDate,endingDate)
    const compoundInterest = calculateCompoundInterest(principal, dailyInterest, startingDate,endingDate)
    // console.log(simpleInterest, compoundInterest);

    const extraAmount = compoundInterest - simpleInterest
    const percentage = (extraAmount/simpleInterest)*100


    return Math.floor(percentage);

}
// console.log(extraAmountPercentage(20000,1,"2020-12-27","2021-08-27"))

setTimeout (() => console. log( 'hello from setTimeOut one'), 0)
console. log( 'hello for main one')
setTimeout (() => console. log( 'hello from setTimeOut two'), 0)
console. log( 'hello from main two')

setTimeout(() => {
    document.getElementById('id').style.backgroundColor = 'red'
}, 10)

let startNamePrinter = (name) => {1
    let x = name.split('').reverse()
    let handler = setInterval(() => {
        let y = x. pop ()
        console.log((y))
    }, 1000)
    setTimeout ( () => {
        clearInterval (handler)
    }, (name.length + 1)*1000)
}

startNamePrinter('orange')