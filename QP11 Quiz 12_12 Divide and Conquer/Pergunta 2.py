def find_me(f, limits):
    mid = (limits[0] + limits[1])//2
    result = f(mid)
    if result == 0:
        return 1
    if result == -1:
        return 1 + find_me(f, (limits[0], mid - 1))
    # if result == 1:
    return 1 + find_me(f, (mid + 1, limits[1]))