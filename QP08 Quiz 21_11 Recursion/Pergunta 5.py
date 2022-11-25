def soup(matrix, word):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #easiest case (where the word is only one letter)
            if matrix[i][j] == word:
                return str(chr(i + 65)) + str(j)
            #find the position of the first character of the word
            if matrix[i][j] == word[0]:
                if soup2(matrix, word[1:], i, j):
                    return str(chr(i + 65)) + str(j + 1)


def soup2(matrix, word, line, column):
    
    #base case
    if word == "":
        return True
    
    #verificar linha acima, linha abaixo, coluna a esquerda coluna a direita
    if line != 0:
        #check top
        if matrix[line - 1][column] == word[0]:
            return soup2(matrix, word[1:], line - 1, column)
    
    if line != len(matrix) - 1:
        #check bottom
        if matrix[line + 1][column] == word[0]:
            return soup2(matrix, word[1:], line + 1, column)
    
    if column != 0:
        #check left
        if matrix[line][column - 1] == word[0]:
            return soup2(matrix, word[1:], line, column - 1)
        
    if column != len(matrix[0]) - 1:
        #check right
        if matrix[line][column + 1] == word[0]:
            return soup2(matrix, word[1:], line, column + 1)
    return False