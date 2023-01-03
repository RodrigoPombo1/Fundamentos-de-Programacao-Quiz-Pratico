def number_of_collisions(objects):
    result = 0
    for i in range(len(objects) - 1):
        for j in range(i + 1, len(objects)):
            if collides(objects[i], objects[j]):
                result += 1
    return result

def collides(obj1, obj2):
    counter = 0
    for i, j in [("x1","x2"), ("y1", "y2")]:
        if obj1[j] < obj2[i] or obj2[j] < obj1[i]:
            return False
    return True
