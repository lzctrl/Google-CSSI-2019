// function helloWorld() {
//   for (i = 0; i < 1000; i++) {
//     let r = Math.random() * 5
//     let w = Math.random() * 9
//     console.log(r * w);
//   }
// }

// Js intro

// Square roof of a^2 + b^2
let a = 10;
let b = 15;

let c_squared = a*a + b*b;
console.log(Math.sqrt(c_squared));

function showDrive() {
  var age = document.getElementById('age').value;

  if (age === "") {
    console.log("Empty");
  } else if (age >= 16 && age <= 100) {
    console.log("You can drive");
  } else {
    console.log("You can't drive");
  }
}

function finalGrade() {
  let a_limit = 90;
  let b_limit = 80;
  let c_limit = 70;
  let d_limit = 60;

  let score = document.getElementById('score').value

  let finalGrade = ""

  if (score > c_limit) {
    console.log("You Passed");
    if (score > a_limit) {
      console.log("with a A");
    } else if (score > b_limit) {
      console.log("with a B");
    } else {
      console.log("with a C");
    }
  } else if (score > d_limit) {
    console.log("You got a D");
  } else {
    console.log("You failed");
  }
}
