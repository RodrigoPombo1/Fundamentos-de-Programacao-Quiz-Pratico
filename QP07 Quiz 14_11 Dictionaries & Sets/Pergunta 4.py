def isomorphic(astring1, astring2):
    result_list = []
    for counter, char in enumerate(astring1):
        tuple_aux = (char, astring2[counter])
        #checks if the element already exists
        if tuple_aux not in result_list:
            for element in result_list:
                if tuple_aux[0] == element[0] or tuple_aux[1] == element[1]:
                    return(f"'{astring1}' and '{astring2}' are not isomorphic")
            result_list.append(tuple_aux)
    return f"'{astring1}' and '{astring2}' are isomorphic because we can map: {result_list}"