def variance(alist):
    length = len(alist)
    average = sum(alist)/length
    return round(sum(map(lambda x: (x - average)**2, alist))/length, 3)
