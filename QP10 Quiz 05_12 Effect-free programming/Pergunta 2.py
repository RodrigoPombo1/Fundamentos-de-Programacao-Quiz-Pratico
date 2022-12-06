from math import sqrt

def comprehensions(i, j):
    lst_num_3_8 = [x for x in range(i, j+1) if x % 10 == 3 or x % 10 == 8]
    sqrt_num = tuple([round(sqrt(x),2) for x in range(i, j+1)])
    dict_ascii = {x: chr(x) for x in range(i, j+1)}
    return (lst_num_3_8, sqrt_num, dict_ascii)