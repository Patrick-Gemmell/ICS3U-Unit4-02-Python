#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: OcTober 2019
# This program adds up a loop counter


def main():
    # This function adds up a loop counter
    integer = input("Enter an integer: ")
    loop_counter = 0
    total = 1

    # inputs
    try:
        integer_as_number = int(integer)
        while loop_counter < integer_as_number:
            print("")
            loop_counter = loop_counter + 1
            total = loop_counter * total
            print("+{0}".format(loop_counter))
        print("")
        print("Your total is {0}".format(total))
    except Exception:
        print("that is not an integer")


if __name__ == "__main__":
    main()
