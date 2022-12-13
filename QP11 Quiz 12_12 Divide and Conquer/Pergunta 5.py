def longest_prefix(words):
    length = len(words)
    if length == 1:
        return words[0]
    if length > 2:
        length = len(words)
        return longest_prefix([longest_prefix(words[:length//2]), longest_prefix(words[length//2:])])
    # if length == 2
    counter = 0
    lenword0 = len(words[0])
    lenword1 = len(words[1])
    if lenword0 < lenword1:
        lengthwrd = lenword0
    else:
        lengthwrd = lenword1
    for i in range(lengthwrd):
        if words[0][i] != words[1][i]:
            break
        counter += 1
    return words[0][:counter]