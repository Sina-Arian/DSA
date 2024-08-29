'''3.The selection sort algorithm sorts a list by finding ...'''


def min(list):
    out = list[0]
    for i in list:
        if i < out:
            out = i
    return out


def selection_sort(list): # theta equals n*2
    n = 0
    finish = len(list) - 1
    while n != finish:
        m = min(list[n:])
        i = list.index(m)
        element = list.pop(i)
        list.insert(n,element)
        n += 1
    return list


lst = [6, 1, 8, 4, 3, 2, 5, 7]
print(selection_sort(lst))