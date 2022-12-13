def msort(xs):
    length = len(xs)
    if length <= 1:
        return xs
    length_2 = length // 2
    sortedsublst0 = msort(xs[:length_2]) 
    sortedsublst1 = msort(xs[length_2:])
    for i in range(length):
        lensorted0 = len(sortedsublst0)
        lensorted1 = len(sortedsublst1)
        if lensorted0 != 0 and lensorted1 != 0:
            if sortedsublst0[0] > sortedsublst1[0]:    
                xs[i] = sortedsublst1.pop(0)
            else:
                xs[i] = sortedsublst0.pop(0)
        elif lensorted0 == 0:
            return xs[:i] + sortedsublst1
        else: # if lensorted1 == 0:
            return xs[:i] + sortedsublst0