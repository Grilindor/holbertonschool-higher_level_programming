#!/usr/bin/python3

def roman_to_int(roman_string):
    # Check if the input is a string and not None
    if not roman_string or roman_string is None:
    # if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary mapping Roman numerals to their integer values
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_val = 0
    # Loop through each character in the Roman numeral string
    for i in roman_string:
        value = rom_num.get(i, 0)
        # If the current value is greater than the previous value, subtract twice the previous value
        if value > prev_val:
            total += value - 2 * prev_val
        else:
            total += value
        prev_val = value
    return total
