##
## EPITECH PROJECT, 2019
## CNA_groundhog_2018
## File description:
## Makefile
##

all:
	cp ex01/hex_to_base64.py challenge01
	cp ex02/fixed_xor.py challenge02
	chmod +x challenge01 challenge02

clean:

fclean: clean
	rm challenge01

re: fclean all