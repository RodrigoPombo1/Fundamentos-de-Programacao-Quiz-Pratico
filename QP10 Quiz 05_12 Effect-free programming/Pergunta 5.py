def distribute(adict, op):
    for key, values in adict.items():
        if values == []:
            yield key
        for value in values:
            yield op(key, value)