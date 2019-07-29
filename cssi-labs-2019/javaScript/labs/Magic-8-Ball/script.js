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

const posReponses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes – definitely", "You may rely on it", "As I see it", "Most Likely", "Outlook good", "Yes", "Signs point to yes"]
const negReponses = ["Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
const nonCommReponses = ["Reply hazy", "Try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]

let ball = document.querySelector("#ball");

let answer = document.querySelector("#answer");

const initBall = () => {
  let answerGiven = ""
  let randomCategory = getRandomNumber(0, 3)
  console.log(randomCategory);
  if (randomCategory === 0) {
    let randomItem = getRandomNumber(0, posReponses.length - 1);
      console.log(randomItem);
    answerGiven = posReponses[randomItem]
  } else if (randomCategory === 1) {
    let randomItem = getRandomNumber(0, negReponses.length - 1);
    console.log(randomItem);
    answerGiven = negReponses[randomItem]
} else {
    let randomItem = getRandomNumber(0, nonCommReponses.length - 1);
    console.log(randomItem);
    answerGiven = nonCommReponses[randomItem]
  }

  answer.innerHTML = answerGiven
}

ball.addEventListener("click", initBall);

document.body.onkeyup = function(e){
    if(e.keyCode == 32){
      initBall();
    }
}

const getRandomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min) + min);
}
