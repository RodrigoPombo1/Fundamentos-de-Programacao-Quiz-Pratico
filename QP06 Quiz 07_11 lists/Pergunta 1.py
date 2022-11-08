def mastermind(guesses, correct):
    length = len(guesses)
    counter = 0
    #checks if he guessed precisely
    n_correct_position = 0
    for i in range(length):
        if guesses[counter] in correct and guesses[counter] == correct[counter]:
            n_correct_position += 1
            correct.pop(counter)
            guesses.pop(counter)
            continue
        counter += 1
            
    counter = 0
    n_incorrect_position = 0
    #checks if one of the things he didn't guessed precisely are just in the wrong position
    for guess in guesses:
        if guess in correct:
            n_incorrect_position += 1
            for i in range(len(correct)):
                if guess == correct[i]:
                    correct.pop(i)
                    break
        counter += 1
    return (n_correct_position, n_incorrect_position)