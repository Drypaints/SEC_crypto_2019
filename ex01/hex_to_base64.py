#!/usr/bin/env python3
import sys
import base64

def converter(hexa):
    if (hexa[-1] == '\n' or hexa[-1] == ' '):
        hexa = hexa[:-1]
    byte = bytes.fromhex(hexa)
    result = base64.b64encode(byte)
    result = str(result)[2:-1]
    return(result)

if __name__ == "__main__":
    take = sys.argv
    
    if len(take) != 2:
        exit(84)
    else:
        in_file = open(take[1], "r")
        hexa = in_file.readline()
        print(converter(hexa))
