#!/usr/bin/env python3
import sys

def find_score(text):
    score = 0
    english_letters = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h','i', 'j', 'k', 'l','m', 'n', 'o', 'p','q', 'r', 's', 't','u', 'v', 'w', 'x','y', 'z', ' ']

    text = str(text)[2:-1]
    for nb_letter in range(len(english_letters)):
        if (text.count(english_letters[nb_letter]) != 0):
            score = score + 1
    return (score)

def decoded_hex(coded):
    score = []

    for key in range(256):
        xored = b''
        for byte in coded:
            xored += bytes([byte ^ key])
    text = score.index(max(score))
    text = str.upper(hex(text))[2:]
    return(text)

if __name__ == "__main__":
    take = sys.argv
    if len(take) != 2:
        exit (84)
    with open(take[1], "r") as in_file:
        coded = in_file.readline().replace('\n','')
        coded = bytes.fromhex(coded)
        print(decoded_hex(coded))
