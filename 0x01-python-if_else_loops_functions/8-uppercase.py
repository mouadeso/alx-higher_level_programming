#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase letters to uppercase by adjusting ASCII code
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        print(upper_char, end="")
    print()
