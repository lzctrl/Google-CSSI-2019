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

// console.log("script is running...");

// Tasks

const My_Alarm = (wakingTime) => {
  return "Hey, Mikhail, wake up! It's " + wakingTime;
};

const Mom_Alarm = (wakingTime) => {
  return "Hey, Mom, wake up! It's " + wakingTime;
};

const Family_Alarm = (name, wakingTime) => {
  return "Hey, " + name + ", wake up! It's " + wakingTime;
};

const Important_Alarm = (message) => {
  return message.toUpperCase();
};

const Snooze_Alarm = (time) => {
  let newTime = time + 1
  return "The alarm for " + time + " has been changed to " + newTime;
};


// Extension

const wakeNumberOfPeople = (numOfPeople) => {
  for ( i = 0; i < numOfPeople; i++ ) {
    console.log("Wake up!");
  }
}

// Call the functions above

console.log(My_Alarm("8:00am"));

console.log(Mom_Alarm("9:00am"));

console.log(Family_Alarm("Mikhail", "8:00am"));

console.log(Important_Alarm("wake up"));

console.log(Snooze_Alarm(8));

console.log(wakeNumberOfPeople(15));
