def change(amount):
    list_result = []
    while amount >= 200:
        list_result.append(200)
        amount -= 200
    while amount >= 100:
        list_result.append(100)
        amount -= 100
    while amount >= 50:
        list_result.append(50)
        amount -= 50
    while amount >= 20:
        list_result.append(20)
        amount -= 20
    while amount >= 10:
        list_result.append(10)
        amount -= 10
    while amount >= 5:
        list_result.append(5)
        amount -= 5
    while amount >= 2:
        list_result.append(2)
        amount -= 2
    while amount >= 1:
        list_result.append(1)
        amount -= 1
    return list_result