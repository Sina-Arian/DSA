def max(lst):
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    
    elif len(lst) == 1:
        return lst[0]

    else:
        mid = len(lst) // 2
        return max( [max(lst[:mid]), max(lst[mid:])])



lst = [102, 3, 71, 23, 70, 1, 80, 9, 100, 1]

print(max(lst))