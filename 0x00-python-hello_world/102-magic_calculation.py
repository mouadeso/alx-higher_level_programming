#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result += a  # LOAD_FAST 0 (a)
    result = result ** b  # BINARY_POWER
    result += a  # BINARY_ADD
    return result  # RETURN_VALUE

# Check if it produces the same bytecode
dis.dis(magic_calculation)

