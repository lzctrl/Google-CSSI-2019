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

let currentlily = 1;

const frogger = document.querySelector("#frog");
const lilyPad1 = document.querySelector("#lilypad1");
const lilyPad2 = document.querySelector("#lilypad2");
const lilyPad3 = document.querySelector("#lilypad3");
const lilyPad4 = document.querySelector("#lilypad4");
const lilyPad5 = document.querySelector("#lilypad5");

const winText = document.querySelector("#name");

winText.style.display = "none";

frogger.addEventListener("click", (e) => {
  currentlily += 1;
  executeLevel(currentlily)
});

const executeLevel = (lily) => {
  if (lily === 1) {
    resetLevel()
  } else if (lily === 2) {
    winText.style.display = "none";
    frog.style.left = "33.5%";
    frog.style.top = "24%";
    lilypad1.style.border = "none";
    lilyPad2.style.border = "solid yellow thick";
  } else if (lily === 3) {
    frog.style.left = "50%";
    frog.style.top = "50%";
    lilypad2.style.border = "none";
    lilyPad3.style.border = "solid yellow thick";
  } else if (lily === 4) {
    if (!checkLilyVisibilityLose()) {
      frog.style.left = "68%";
      frog.style.top = "75%";
      lilypad3.style.border = "none";
      lilyPad4.style.border = "solid yellow thick";
    }
  } else if (lily === 5) {
    winText.style.display = "block";
    winText.innerHTML = "You Win!";
    frog.style.left = "83%";
    frog.style.top = "50%";
    lilypad4.style.border = "none";
    lilyPad5.style.border = "solid yellow thick";
  } else {
    resetLevel()
  }
}

const checkLilyVisibilityLose = () => {
  if (lilypad4.style.display === "none") {
    winText.style.display = "block";
    winText.innerHTML = "You Lose";
    resetLevel()
    return true
  }

  return false
}

const resetLevel = () => {
  currentlily = 1
  frog.style.left = "17%";
  frog.style.top = "50%";
  lilypad2.style.border = "none";
  lilypad3.style.border = "none";
  lilypad4.style.border = "none";
  lilypad5.style.border = "none";
  lilyPad1.style.border = "solid yellow thick";
  winText.style.display = "none";
}

document.body.onkeyup = function(e) {
  if (e.keyCode == 32) {
    currentlily += 1;
    executeLevel(currentlily)
  }
}

let isLilyHidden = false

setInterval(() => {
  isLilyHidden = !isLilyHidden
  if (isLilyHidden) {
    lilyPad4.style.display = "none";
    if (frog.style.left === "68%" && frog.style.top === "75%") {
      winText.style.display = "block";
      winText.innerHTML = "You Lose";
      resetLevel()
    }
  } else {
    lilyPad4.style.display = "block";
  }
}, 1000);
