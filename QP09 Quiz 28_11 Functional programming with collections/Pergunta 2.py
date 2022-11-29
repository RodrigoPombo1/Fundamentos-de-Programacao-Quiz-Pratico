def differences(alist):
    tuple_elements = map(lambda x: x[0] - x[1],list(zip(alist[1:], alist)))
    return list(tuple_elements)