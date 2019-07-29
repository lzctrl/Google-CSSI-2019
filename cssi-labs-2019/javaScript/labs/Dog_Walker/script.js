// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Functions used in this document

const printAppointment = (dogName, hour) => {
  console.log("I will walk " + dogName + " today at " + hour);
};

const favoriteAppointment = (dogName, hour) => {
  console.log("I will walk, one of my favorite dogs, " + dogName + " today at " + hour);
};

const capitalizeFirstLetter = (string) => {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

// Task 1
const dogName1 = "Steve";
const dogType1 = "beagle";

printAppointment(dogName1, "12:00pm");

// Task 2
const dogName2 = "Joe";
const dogType2 = "poodle";

if (dogType2 === "corgi") {
  printAppointment(dogName2, "12:00pm");
} else {
  printAppointment(dogName2, "1:00pm");
}

// Task 3
const dogName3 = "Lola";
const dogType3 = "poodle";

let time_walking = ""

if ( dogType3 === "corgi" || dogType3 === "beagle" ) {
  printAppointment(dogName3, "12:00pm");
  time_walking = "12:00pm";
} else if ( dogType3 === "bulldog" ) {
  printAppointment(dogName3, "1:00pm");
  time_walking = "1:00pm";
} else {
  printAppointment(dogName3, "2:00pm");
  time_walking = "2:00pm";
}


// Extension

let dogName = dogName3.toLowerCase()

if ( dogName === "spike" || dogName === "jeremy" || dogName === "lola" || dogName === "peaches" || dogName === "steve") {
  favoriteAppointment(capitalizeFirstLetter(dogName), time_walking)
}

// Function practices

const pythagoreanTheorem = (a, b) => {
  let ans = Math.sqrt((Math.pow(a, 2) + Math.pow(b, 2)))
    console.log("Inputing " + a + " and " + b + " into the pythagorean theorem will result in c being: " + ans);
};

let a = Math.round((Math.random() * 9) + 1);
let b = Math.round((Math.random() * 9) + 1);

// Calling functions

pythagoreanTheorem(a, b);
