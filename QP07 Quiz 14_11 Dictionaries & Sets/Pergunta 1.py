def switch_dict(adict):
    result_dict = {}
    for key, value in adict.items():
        if value not in result_dict.keys():
            result_dict[value] = [key]
        else:
            result_dict[value].append(key)
    return result_dict