from TreeNode import TreeNode

class BST():
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, item):
        if self.root is None:
            self.root = TreeNode(item)
            self.length += 1

        else:
            node = self.root
            while True:
                if item == node.item:
                    raise ValueError("Inserting duplicate item")
                
                if item < node.item:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = TreeNode(item)
                        self.length += 1
                        break
                
                else:
                    if node.right is not None:
                        node = node.right
                    else:
                        node.right = TreeNode(item)
                        self.length += 1
                        break
    
    def insert_rec(self, item):
        self.root = self._subtreeInsert(self.root, item)
        
    def _subtreeInsert(self, root, item):
        if root is None:
            self.length += 1
            return TreeNode(item)
        
        if item == root.item:
            raise ValueError("Inserting duplicated item")
        
        if item < root.item:
            root.left = self._subtreeInsert(root.left, item)
        
        else:
            root.right = self._subtreeInsert(root.right, item)
        
        return root

    def find_rec(self, item):
        try:
            return self._findrecursive(self.root, item)
        except:
            return None

    def _findrecursive(self, root, item):
        if root.item is None:
            return None
        
        if root.item == item:
            return root.item
        else:
            if root.item > item:
                return self._findrecursive(root.left, item)
            else:
                return self._findrecursive(root.right, item)

    def find(self, item):
        node = self.root
        while node is not None and node.item != item:
            if node.item > item:
                node = node.left
            
            else:
                node = node.right

        if node is None:
            return None
        else:
            return node.item

    def _subtreeDelete_successor(self, root, item):
        if root is None:
            return None
        if item < root.item:
            root.left = self._subtreeDelete(root.left, item)
        elif item > root.item:
            root.right = self._subtreeDelete(root.right, item)
        else:
            if root.left is None:
                root = root.right
                self.length -= 1
            elif root.right is None:
                root = root.left
                self.length -= 1
            else:
                root.item, root.right = self._subtreeDelMax_successor(root.right)
                self.length -= 1
        return root

    def _subtreeDelMax_successor(self, root):
        if root.left is None:
            return root.item, root.right
        else:
            maxVal, root.left = self._subtreeDelMax_successor(root.left)
            return maxVal, root

    def delete(self, item):
        '''pre-condition: the item should be in the Tree
           post-condition: the item get deleted'''
        method = input("deleting by precede or succuss: ")
        assert method == 'precede' or method == 'succuss'
        if method == 'precede':
            self.root = self._subtreeDelete(self.root, item)
        elif method == 'succuss':
            self.root = self._subtreeDelete_successor(self.root, item)

    def _subtreeDelete(self, root, item):
        if root is None:
            return None
        if item < root.item:
            root.left = self._subtreeDelete(root.left, item)
        elif item > root.item:
            root.right = self._subtreeDelete(root.right, item)
        else:
            if root.left is None:
                root = root.right
                self.length -= 1
            elif root.right is None:
                root = root.left
                self.length -= 1
            else:
                root.item, root.left = self._subtreeDelMax(root.left)
                self.length -= 1
        return root

    def _subtreeDelMax(self, root):
        if root.right is None:
            return root.item, root.left
        else:
            maxVal, root.right = self._subtreeDelMax(root.right)
            return maxVal, root
    

    def __iter__(self):
        return self._inorderGen(self.root)

    def _inorderGen(self, root):
        if root is not None:
            for item in self._inorderGen(root.left):
                yield item

            yield root.item

            for item in self._inorderGen(root.right):
                yield item

    def preOrder(self):
        return self._preOrderGen(self.root)

    def _preOrderGen(self, root):
        if root is not None:
            yield root.item

            for item in self._preOrderGen(root.left):
                yield item

            for item in self._preOrderGen(root.right):
                yield item

    def postOrder(self):
        return self._postOrderGen(self.root)

    def _postOrderGen(self, root):
        if root is not None:

            for item in self._postOrderGen(root.left):
                yield item

            for item in self._postOrderGen(root.right):
                yield item

            yield root.item

    def __copy__(self):
        out = BST()
        for i in self:
            out.insert(i)
        return out

    def __len__(self):
        return self.length