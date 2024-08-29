class ListNode():
    def __init__(self, data = None, link = None, before = None):
        self.data = data
        self.link = link
        self.before = before


class LList():
    
    def __init__(self, seq = ()):
        if seq == ():
            self.head = None
            self.last = self.head
        else:
            self.head = ListNode(seq[0])
            self.last = self.head
            for i in seq[1:]:
                self.last.link = ListNode(i, None, self.last)
                self.last = self.last.link

        self.size = len(seq)

    def __len__(self): # now you can say len(a)
        return self.size

    def _find(self, position):  
        assert 0 <= position < self.size
        node = self.head
        for i in range(position):
            node = node.link
        return node

    def append(self, x):
        if self.head is None:
            self.head = ListNode(x)
            self.last = self.head
            self.size += 1
        else:
            self.last.link = ListNode(x, None, self.last)
            self.last = self.last.link
            self.size += 1
    
    def __getitem__(self, position):
        node = self._find(position)
        return node.data

    def __setitem__(self, position, value):
        node = self._find(position)
        node.data = value
    
    def __deleteitem__(self, position):
        assert 0 <= position < self.size
        self._delete(position)

    def _delete(self, position):
        if position == 0: #chonke oon paeen position -1 dari bekhatere hamin bayad jodagane baraye 0 ro tarif koni
            item = self.head.data
            self.head = self.head.link
            self.head.before = None

        elif position == self.size - 1:
            prev_node = self.last.before
            item = prev_node.link.data
            prev_node.link = prev_node.link.link #bayad None bashe
            self.last = prev_node

        else:
            prev_node = self._find(position-1)
            item = prev_node.link.data
            prev_node.link = prev_node.link.link
            prev_node.link.before = prev_node

        self.size -= 1
        return item

    def pop(self, i = None):
        assert self.size > 0 and (i is None or (0 <= i< self.size))
        if i is None:
            i = self.size - 1
        return self._delete(i)

    def insert(self, i , x):
        assert 0 <= i <= self.size
        if i == 0:
            new_node = ListNode(x, self.head)
            self.head.before = new_node
            new_node = self.head
        elif i == (self.size - 1):
            self.append(x)
        else:
            prev_node = self._find(i-1)
            new_node = ListNode(x, prev_node.link, prev_node)
            prev_node.link.before = new_node
            prev_node.link = new_node
        self.size += 1

    def __copy__(self):
        a = LList()
        node = self.head
        while node is not None:
            a.append(node)
            node = node.link
        return a

    def __min__(self):
        min = self.head.data
        next = self.head.link
        while next is not None:
            if min > next:
                min = next
            next = next.link
        return min

    def __max__(self):
        max = self.head.data
        next = self.head.link
        while next is not None:
            if max < next:
                max = next
            next = next.link
        return max

    def index(self, x):
        try:
            target = self.head
            i = 0
            while target.data is not x:
                target = target.link
                i += 1
            return i
        except:
            return "There is no {x}!".format(**locals())

    def count(self, x):
        c = 0
        node = self.head
        while True:
            if node.data is x:
                c += 1
            if node.link is None:
                break
            else:
                node = node.link
        return c

    def remove(self, x):
        if self.head.data is x:
            self.head = self.head.link
            self.head.before = None
            self.size -= 1
        else:
            try:
                target = self.head
                while target.data is not x:
                    prev = target
                    target = target.link
                if target is self.last:
                    self.last = prev
                prev.link = target.link
                if target.link is not None:
                    target.link.before = prev

                self.size -= 1
            except:
                print("There is no {x}!".format(**locals()))

    # def __copy__(self):
    #     a = []
    #     node = self.head
    #     while node is not None:
    #         a.append(node)
    #         node = node.link
    #     return LList(a)
        

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.link

    # def __next__(self):
    #     self.currNode  = self.last
    #     if self.currNode is None:
    #         raise StopIteration
    #     else:
    #         data = self.currNode.data
    #         self.currNode = self.currNode.before
    #         return data

    def reverse_iter(self):
        self.currNode  = self.last
        while self.currNode is not None:
            yield self.currNode.data
            self.currNode = self.currNode.before


# lst = [1, 2, 3, 4, 5]
# myLList = LList(lst)
# for i in myLList.reverse_iter():
#     print(i)


# class LListIterator():
#     def __init__(self, head):
#         self.currNode  = head

#     def next(self):
#         if self.currNode is None:
#             raise StopIteration
        
#         else:
#             data = self.currNode.data
#             self.currNode = self.currNode.link
#             return data
