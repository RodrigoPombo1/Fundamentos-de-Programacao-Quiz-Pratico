def tic_tac_toe(board, player):
    matrix = [[],[],[]]
    counter = 0
    for char in board:
        if char == "\n":
            counter += 1
            continue
        matrix[counter].append(char)
    for count_line in range(len(matrix)):
        for count_element in range(len(matrix[0])):
            if matrix[count_line][count_element] == " ":
                matrix2 = matrix.copy()
                matrix2[count_line][count_element] = player
                if check(matrix2):
                    return chr(ord("A") + count_line) + str(count_element + 1)
                
def check(matrix):
    for line in matrix:
        if line[0] == line[1] and line[1] == line[2]:
            return True
    for count_column in range(len(matrix[0])):
        if matrix[0][count_column] == matrix[1][count_column] and matrix[1][count_column] == matrix[2][count_column]:
            return True
    if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]):
        return True
    return False
