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

let customerName;
let balance;

const openAccount = (name, startingBalance = 0) => {
  balance = 0;
  // Set the value for customer_name equal to name below
  customerName = name;
  balance = startingBalance;
  return name + " has opened a new account with a balance of $" + startingBalance;
};

const deposit = (value) => {
  // update the value of balance
  //return the correct statement
  balance += value;
  return customerName + " has deposited " + value + ". " + customerName + "\'s total balance is $" + balance;
};

const withdraw = (value) => {
  //update the value of balance
  //return the correct statement

  if (value > balance) {
    let diff = value - balance;
    return "Sorry, " + customerName + ", you do not have enough money in your account. You need " + diff +  " more dollars."
  }

  balance -= value;
  return customerName + " has withdrawn " + value + ". " + customerName + " has $" + balance + " remaining.";
};

// Write your script below
console.log(openAccount("Mikhail", 300));
console.log(deposit(50));
console.log(withdraw(500));

console.log(withdraw(150));
