def flatten(alist):
    if alist == []:
        return alist
    if type(alist[0]) is list:
        return flatten(alist[0]) + flatten(alist[1:])
    else:
        return[alist[0]] + flatten(alist[1:])