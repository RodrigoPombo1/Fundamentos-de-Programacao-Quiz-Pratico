import functools

def bounding_box(pts):
    return (tuple(functools.reduce(lambda a, b: a if (a[0]<b[0]) else b, pts))[0], tuple(functools.reduce(lambda a, b: a if (a[1]<b[1]) else b, pts))[1], tuple(functools.reduce(lambda a, b: a if (a[0]>b[0]) else b, pts))[0], tuple(functools.reduce(lambda a, b: a if (a[1]>b[1]) else b, pts))[1])
