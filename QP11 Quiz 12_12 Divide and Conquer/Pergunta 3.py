def search_tree(key, tree, visited=[]):
    if tree == None:
        for _ in range(len(visited)):
            visited.pop()
        return None
    visited.append(tree[0])
    if key == tree[0]:
        visited2 = visited.copy()
        for _ in range(len(visited)):
            visited.pop()
        return (tree[1], visited2)
    if key < tree[0]:
        return search_tree(key, tree[2], visited)
    # if key > tree[0]:
    return search_tree(key, tree[3], visited)
