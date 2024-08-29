def squeeze(lst):
    out = []
    for i in lst:
        if test(i, out) == False:
            out.append(i)
    return out

def test(i, lst):
    for t in lst:
        if i == t:
            return True
    return False


x = [1, 1, 3, 3, 3, 3, 3, 4, 5, 5, 8, 9, 9, 9, 9, 9, 10, 10]
print(squeeze(x))
