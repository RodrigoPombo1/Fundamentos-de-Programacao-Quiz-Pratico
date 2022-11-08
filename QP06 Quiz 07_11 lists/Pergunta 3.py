def local_minima(alist):
    counter = 0
    result_list = []
    for i in range(len(alist) - 2):
        list_3_elements = alist[counter:counter+3]
        local_minima = get_local_minima(list_3_elements)
        if local_minima != False:
            result_list.append(local_minima[0])
        counter += 1
    return result_list
    
def get_local_minima(list_3_elements):
    result_list = [list_3_elements[0]]
    return_result = True
    for i in range(1, 3):
        if result_list[0] > list_3_elements[i]:
            result_list[0] = list_3_elements[i]
            return_result = True
        elif result_list[0] == list_3_elements[i]:
            return_result = False
    if return_result == True:        
        return result_list
    else:
        return False