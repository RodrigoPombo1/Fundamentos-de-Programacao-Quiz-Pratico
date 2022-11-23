#eu fiz só com recursão pq pensava que não se podiam usar for loops então pronto, a minha solução é extremamente complicada

def file_finder(dirs, file_name):
    #base case (if the file is already in the selected folder)
    if file_name in dirs:
        if not (len(dirs) == 2 and type(dirs[0]) == str and type(dirs[1]) == list):
            return file_name
    
    #checks if the current directory is a folder
    if len(dirs) == 2:
        if type(dirs[0]) == str and type(dirs[1]) == list:
            result = file_finder(dirs[1], file_name)
            if result is not None:
                return dirs[0] + "/" + result
    
    #checks if the first file or folder in the directory is a folder
    if len(dirs) > 0:
        if type(dirs[0]) == tuple:
            result = file_finder(dirs[0], file_name)
            if result is not None:
                return result

    #in the case where there are more than one folder or file in the current directory (and the current directory isn't a folder)
    if len(dirs) > 1:
        #runs the function on the rest of the files or folders in the current directory
        return file_finder(dirs[1:], file_name)