def primes_range(start, stop):
    for x in range(start, stop + 1):
        is_prime = True
        for i in range(2, x//2 + 1):
            if x % i == 0 and i != 1:
                is_prime = False
                break
        if is_prime == True and x != 1:
            yield x