def check_results(bet, results):
    hits = 0
    for counter, element in enumerate(results):
        if element[2] == element[3] and bet[counter] == "X":
            hits += 1
        elif element[2] > element[3] and bet[counter] == "1":
            hits += 1
        elif element[2] < element[3] and bet[counter] == "2":
            hits += 1
    return hits