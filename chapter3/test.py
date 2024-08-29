def insertion_sort(lst:list, new:int):
    if lst == []:
        lst.append(new)
    else:
        for item in lst:
            _in = False
            if new > item:
                ind = lst.index(item)
                lst.insert(ind, new)
                _in = True
                break

        if _in == False:
            lst.append(new)
            
    return lst
