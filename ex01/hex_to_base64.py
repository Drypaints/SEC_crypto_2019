#!/usr/bin/env python3
from sys import argv
from binascii import b2a_base64, unhexlify

def convert_hex_to_base64(string_to_decode):
    result = str(b2a_base64(unhexlify(string_to_decode.strip(' \n'))))
    return result

if __name__ == "__main__":
    if len(argv) != 2:
        exit(84)
    with open(argv[1]) as in_file:
        file_content = in_file.readline()
        print(convert_hex_to_base64(file_content))
