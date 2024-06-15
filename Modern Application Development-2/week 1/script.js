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
    

    var yes = new Date(startingDate);
    var tod = new Date(endingDate);
    var diff = tod - yes;
    var diffDays = diff/ (1000*60*60*24)
  
    const interest = (principal*dailyInterest*diffDays) / 100;
  
    return Math.floor(interest);
  
  }

console.log(calculateSimpleInterest(20000, 1, "2020-12-27", "2021-08-27"))



  function calculateCompoundInterest(
    principal,
    dailyInterest,
    startingDate,
    endingDate
  ) {
  
  // Add your code here
  
//   return Math.floor(interest);
  
  }
  
  function extraAmountPercentage(
    principal,
    dailyInterest,
    startingDate,
    endingDate
  ) {
  
  // Add your code here
  
//   return Math.floor(percentage);
  
  }
  