#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_len = len(roman_string)
    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subtractive_forms = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    total = value = i = 0
    while i < roman_len:
        if roman_string[i] in roman_numerals:
            if i != roman_len - 1:
                sub = roman_string[i] + roman_string[i + 1]
                value = subtractive_forms.get(sub, 0)
            total += value + 0 if value != 0 else roman_numerals.get(
                    roman_string[i])
            if value != 0:
                i += 2
            else:
                i += 1
        else:
            return
    return total
