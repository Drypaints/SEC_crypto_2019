#!/usr/bin/env python3
import sys
import binascii as bin_ascii

def converter(hexa):
    if (hexa[-1] == '\n' or hexa[-1] == ' '):
        hexa = hexa[:-1]
    result = bin_ascii.b2a_base64(bin_ascii.unhexlify(hexa))
    result = str(result)
    result = result[:-3]
    result = result[2:]
    print(result)
    
def main():
    take = sys.argv
    
    if len(take) != 2:
        exit(84)
    else:
        in_file = open(take[1], "r")
        hexa = in_file.readline()
        converter(hexa)
    exit(0)
    
if __name__ == "__main__":
    main()
