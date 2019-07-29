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

// console.log("Running Click Events Script");

const box1 = document.querySelector("#box1");
const box2 = document.querySelector("#box2");
const box3 = document.querySelector("#box3");

const selectingBox = (color) => {
  box1.style.background = color;
  box2.style.background = color;
  box3.style.background = color;
}

box1.addEventListener("click", () => {
    selectingBox("red");
});

box2.addEventListener("click", () => {
  selectingBox("pink");
});

box3.addEventListener("click", () => {
  selectingBox("orange");
});



const box4 = document.querySelector("#box4");
const box5 = document.querySelector("#box5");

let box4Active = false;
let box5Active = false;

box4.addEventListener("click", () => {
  if (box4Active === false) {
    box4Active = true;
    box4.style.background = "blue";
  } else {
    box4Active = false;
    box4.style.background = "yellow";
  }
});

box5.addEventListener("click", () => {
  if (box5Active === false) {
    box5Active = true;
    box5.style.background = "yellow";
  } else {
    box5Active = false;
    box5.style.background = "blue";
  }
});
