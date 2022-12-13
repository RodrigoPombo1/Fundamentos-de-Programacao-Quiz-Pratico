def bisect(f, n):
    lower = 0
    upper = 1
    for i in range(n):
        midpoint = (lower + upper) / 2
        eval_mid = f(midpoint)
        eval_lower = f(lower)
        if (eval_mid < 0 and eval_lower < 0) or (eval_mid > 0 and eval_lower > 0):
            lower = midpoint
        else:
            upper = midpoint
    return round(midpoint, 5)