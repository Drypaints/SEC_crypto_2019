##
## EPITECH PROJECT, 2019
## SEC_crypto_2019
## File description:
## reader
##

def get_file_info(file):
    values = []
    with open(file) as nb_list:
        for line in nb_list:
            values = values + line.split(' ')
    return list(map(lambda x:float(x), values))
