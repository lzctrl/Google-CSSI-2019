const myFunction = () => {
  console.log("Happy thursday");
}

const test = (word) => {
  console.log(word);
}

// setInterval(myFunction, 2500);
//
// setInterval(() => {
//   console.log("I am using an anonymous func");
// }, 1000);

// setInterval( () => {
//   test(new Date())
// }, 1000)
//
// setInterval(function() {
//   test("hi");
// }, 5000)

// Sorting an array

let arr = [101, 3, 4, 1, 6, 8, 10, 5, 60, 100, 87, 55, 55, 28, 26, 49, 10, 44, 25, 19];

for (let i = 0; i < arr.length; i++) {
  for(let j = 0; j <= i; j++) {
    if (arr[i] < arr[j]) {
      let jItem = arr[j];
      arr[j] = arr[i];
      arr[i] = jItem;
    }
  }
}

console.log(arr);

// Finding a number

let specialNum = 26

let low = 0;
let high = arr.length - 1;
// let halfVal = (arr.length - 1) / 2

while (high >= low) {
  let mid = (low + high) / 2;

  if (specialNum < arr[mid]) {
    high = mid - 1;
  } else if (specialNum >= arr[mid]) {
    low = mid + 1;
  } else {
    console.log(mid);
    break;
  }
}
