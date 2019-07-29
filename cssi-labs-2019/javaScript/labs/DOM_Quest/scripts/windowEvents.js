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

console.log("Running Window Events Script");

let box6 = document.querySelector("#box6");
let rect = document.querySelector("#rect");
let congratsText = document.querySelector("#congratsText");

window.addEventListener("keypress", (e) => {
  console.log(e.keyCode);
  if (e.keyCode === 99) {
    box6.style.borderRadius = "50%";
    box6.style.width = "50px";
    box6.style.height = "50px";
  } else if (e.keyCode === 115) {
    box6.style.borderRadius = "100%";
    box6.style.width = "100px";
    box6.style.height = "100px";
  }
});

window.onscroll = function(ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 50) {
       rect.style.background = "#000";
       congratsText.style.display = "block";
    }
    else {
      rect.style.background = "tomato";
      congratsText.style.display = "none";
    }
};
