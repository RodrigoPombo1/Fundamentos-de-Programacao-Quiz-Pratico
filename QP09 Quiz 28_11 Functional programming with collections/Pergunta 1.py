def sort_pairs(alist):
    alist = sorted(alist)
    alist = sorted(alist, key=lambda x: x[1])
    return alist
    
# ou então tudo de uma só vez:
# def sort_pairs(alist):
#     alist = sorted(alist, key=lambda x: (x[1],x[0]))
#     return alist