from Queue import Queue

def queueInOrder(q):
    res = True
    for i in range(q.size()-1):
        a = q.dequeue()
        b = q.top()
        if a > b:
            res = False
        q.inqueue(a)

    q.inqueue(q.dequeue())

    return res



def permInOrder(p):
    res = True
    for i in range(len(p)-1):
        a = p.pop(0)
        b = p[0]
        if a > b:
            res = False
        p.append(a)
    
    p.append(p.pop(0))

    return res


def main():
    q = Queue()
    for i in range(10):
        q.inqueue(i)
    q.inqueue(3)
    print(queueInOrder(q))


if __name__ == "__main__":
    main()
