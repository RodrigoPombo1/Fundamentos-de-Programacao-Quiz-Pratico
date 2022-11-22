def max_path(tree):
    if type(tree) is int:
        return tree
    else: #if type tree is another tree
        max_path_1st_branch = max_path(tree[0]) + tree[1]
        max_path_2nd_branch = tree[1] + max_path(tree[2])
        if max_path_1st_branch > max_path_2nd_branch:
            return max_path_1st_branch
        else:
            return max_path_2nd_branch