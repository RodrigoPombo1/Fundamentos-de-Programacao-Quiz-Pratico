def square_odds(values):
    lst_str_num = values.split(",")
    return ",".join([str(int(x)**2) for x in lst_str_num if (int(x) % 2 != 0)])