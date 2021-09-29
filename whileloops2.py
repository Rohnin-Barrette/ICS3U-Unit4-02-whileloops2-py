#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program factorial of an inputted positive integer


def main():
    # This program factorial of an inputted positive integer

    # this is to keep track of how many times you go through the loop
    loop_counter = 1
    product = 1

    # input
    print("\n", end="")
    positive_string = input("Enter a positive integer: ")

    # process & output
    try:
        positive_number = int(positive_string)
        print("\n", end="")
        if positive_number > 0:
            while loop_counter <= positive_number:
                product = product * loop_counter
                loop_counter = loop_counter + 1
            print("{0}! = {1}".format(positive_number, product))
        else:
            print("Please enter a positive number")
    except Exception:
        print("{0} is not a valid input.".format(positive_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
