def search(items, target):
    low = 0
    high = len(items) - 1 
    while low <= high:
        mid = (high + low) // 2
        if items[mid] == target:
            return mid
        elif items < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    