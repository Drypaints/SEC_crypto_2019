##
## EPITECH PROJECT, 2019
## CNA_groundhog_2018
## File description:
## Makefile
##

all:
	cp hex_to_base64.py challenge01
	chmod +x challenge01

clean:

fclean: clean
	rm challenge01

re: fclean all