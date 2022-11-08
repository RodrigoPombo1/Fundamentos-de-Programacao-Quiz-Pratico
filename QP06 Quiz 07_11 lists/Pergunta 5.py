def mult(M, N):
    result = []
    if len(M[0]) == len(N):
        for i in range(len(M)):
            result.append([])
            for k in range(len(N[0])):
                result_calculation = 0
                for j in range(len(M[0])):
                    result_calculation += M[i][j] * N[j][k]
                result[i].append(result_calculation)
        return result
    else:
        return []