#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase letters to uppercase by adjusting ASCII code
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        result += upper_char
    print("{}".format(result))
