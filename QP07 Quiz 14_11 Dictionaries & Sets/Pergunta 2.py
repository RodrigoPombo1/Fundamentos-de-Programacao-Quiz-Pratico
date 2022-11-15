def sparse_dot_product(dict1, dict2):
    result = 0
    for key, item in dict1.items():
        if key in dict2.keys():
            result += item * dict2[key]
    return result