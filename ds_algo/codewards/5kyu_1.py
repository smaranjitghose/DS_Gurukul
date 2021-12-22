#!/usr/bin/env python3


def parse_int(string: str) -> int:
    # Hash table to store the values of the digits
    n_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    # Declare empty list to store the numbers corresponding to each word
    numbers = []
    # Remove all instances of '-' before parsing
    # Parse the string word by word by splitting it into a list of tokens
    for token in string.replace("-", " ").split(" "):
        # If the token is 1-20 or 30,40,50,60,70,80,90
        if token in n_map:
            # Append the value of the token to the list of numbers
            numbers.append(n_map[token])
        elif token == "hundred":
            # Multiply the last number in the list by 100
            numbers[-1] *= 100
        elif token == "thousand":
            # Multiply all the previous numbers in the list by 1000
            numbers = [n * 1000 for n in numbers]
        elif token == "million":
            # Multiply all the previous numbers in the list by 1000000
            numbers = [n * 1000000 for n in numbers]
    return sum(numbers)
