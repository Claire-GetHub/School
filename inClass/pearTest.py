


def get_values (list1, list2):
    newList = []
    for item in list1 + list1:
        if not item in newList:
            newList.append(item)   
    newList.sort()         
    return newList

