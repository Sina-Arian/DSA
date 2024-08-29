def index_Lsearch(list, target):
    try:
        return list.index(target)
    except:
        return -1


def for_Lsearch(list, target):
    for i in list:
        if i == target:
            return i
    return -1


def Bsearch(list, target):
    low = 0
    high = len(list) 
    while low < high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

