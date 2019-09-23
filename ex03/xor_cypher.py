#!/usr/bin/env python3
import sys

def find_score(text):
    

def decoded_hex(coded):
    possibility = []
    for key in range(256):
        xored = b''
        for byte in coded:
            xored += bytes([byte ^ key])
        
        print(xored) 
    

if __name__ == "__main__":
    take = sys.argv
    if len(take) != 2:
        exit (84)
    with open(take[1], "r") as in_file:
        coded = in_file.readline().replace('\n','')
        coded = bytes.fromhex(coded)
        print(coded)
        decoded_hex(coded)