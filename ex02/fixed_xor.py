#!/usr/bin/env python3
import sys

def xor(hex_one, hex_two):
    result = hex(int(hex_one, 16) ^ int(hex_two, 16))
    result = str(result)[2:]
    result = str.upper(result)
    return(result)

if __name__ == "__main__":
    take = sys.argv
    if len(take) != 2:
        exit (84)
    with open(take[1], "r") as in_file:
        hex_one = in_file.readline().replace('\n','')
        hex_two = in_file.readline().replace('\n','')
        print(xor(hex_one, hex_two))
