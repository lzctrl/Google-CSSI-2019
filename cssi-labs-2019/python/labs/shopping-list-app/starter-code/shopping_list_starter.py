#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

def add_item(item):
    for i in shopping_list:
        if i == item:
            print("That item already exists in this list.")
            return

    shopping_list.append(item)

def remove_item(item):

    check_to_remove = raw_input("Are you sure you would like to remove " + item + "? (y/n) ")

    if check_to_remove == "yes" or check_to_remove == "y":
        removed = False
        for i in range(0, len(shopping_list)):
            if item == shopping_list[i]:
                shopping_list.remove(item)
                removed = True
                break

        if removed == False:
            print("\nThat item was not found in the shopping list\n")

def check_item(item):
    for i in range(0, len(shopping_list)):
        if item == shopping_list[i]:
            return True

    return False

def print_list():
    for i in shopping_list:
        print(i)

while choice.lower() != "e":
    print(" ")
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")
    print(" ")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")

    # Your code below! Handle the cases when the user chooses a, b, c, or d
    if choice == "a":
        print(" ")
        item_adding = raw_input("Please add an item ")

        while item_adding == " ":
            item_adding = raw_input("Please add an item ")

        add_item(item_adding)
    elif choice == "b":
        print(" ")
        item_removing = raw_input("Please remove an item ")

        while item_adding == " ":
            item_removing = raw_input("Please remove an item ")

        remove_item(item_removing)
    elif choice == "c":
        print(" ")
        item_checking = raw_input("Which item do you want to find? ")

        while item_checking == " ":
                item_checking = raw_input("Which item do you want to find? ")

        if check_item(item_checking) == True:
            print("\nThe item was found!\n")
        else:
            print("\nThe item was not found.\n")
    elif choice == "d":
        print(" ")
        if len(shopping_list) != 0:
            print_list()
        else:
            print("The list is empty\n")
