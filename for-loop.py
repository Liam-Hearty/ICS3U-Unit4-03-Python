#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Oct 2019
# This program uses a while loop to add all whole numbers from 1 to the chosen-
# number


def main():
    # this function uses a while loop
    loop_counter = 0
    adding_number = 0
    answer = 0

    # input
    try:
        chosen_number = int(input("Input a positive integer: "))
        print("")

        # process & output
        while loop_counter < chosen_number:
            loop_counter += 1
            print("{0}^2={1}".format(adding_number, answer))
            adding_number += 1
            answer = adding_number*adding_number
        print("{0}^2={1}".format(adding_number, answer))
    except(ValueError):
        print("Please input a positive whole number.")


if __name__ == "__main__":
    main()
