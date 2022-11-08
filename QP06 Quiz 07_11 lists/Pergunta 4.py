def magic(mat):
    sum_lines = check_sum_lines(mat)
    sum_columns = check_sum_columns(mat)
    sum_diagonals = check_sum_diagonals(mat)
    if sum_lines == False or sum_columns == False or sum_diagonals == False:
        return False
    elif sum_lines[0] == sum_columns[0] and sum_lines[0] == sum_diagonals[0] and sum_columns[0] == sum_diagonals[0]:
        return True
    else:
        return False
    
def check_sum_lines(mat):
    result = []
    for i in range(len(mat)):
        sum = 0
        for j in range(len(mat[0])):
            sum += mat[i][j]
        result.append(sum)
        if i > 0:
            if result[0] != sum:
                return False
    return [result[0]]

def check_sum_columns(mat):
    result = []
    for i in range(len(mat)):
        sum = 0
        for j in range(len(mat[0])):
            sum += mat[j][i]
        result.append(sum)
        if i > 0:
            if result[0] != sum:
                return False
    return [result[0]]

def check_sum_diagonals(mat):
    result = []
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][i]
    result.append(sum)
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][len(mat) - i - 1]
    if result[0] != sum:
       return False
    return [result[0]]