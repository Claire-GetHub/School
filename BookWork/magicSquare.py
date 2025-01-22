


def is_magic_square(list2D):
    sum = 0
    for num in list2D[0]:
        sum += num
    
    for list in list2D:
        currentSum = 0
        for num in list:
            currentSum += num
        if not(currentSum == sum):
            return False, "vertical"

    for i in range(len(list2D)):
        currentSum = 0
        for list in list2D:
            currentSum += list[i] 
        if not(currentSum == sum):
            return False, "horizontal"
        
    currentSum = 0
    for list in list2D:  
        currentSum += list[list2D.index(list)]
    if not(currentSum == sum):
        return False, "diagnal 1"  
    currentSum = 0

    list2D.reverse()
    for list in list2D:  
        currentSum += list[list2D.index(list)]
    if not(currentSum == sum):
        return False, "diagnal 2"    

    return True    




list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(is_magic_square(list))

            
        
        
    