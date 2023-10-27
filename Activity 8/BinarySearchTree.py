# Implement a class for a binary search tree
# The class should have a method for adding a node to the tree
# The class should have a method for removing a node from the tree
# The class should have a method to search for a value in the tree

list_items = []

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_value(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.add_value(data)
        elif data > self.data:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.add_value(data)
        else:
            print("Value already in tree")

    def add_values(self, dataList):
        for data in dataList:
            self.add_value(data)
        return self

    def remove_value(self, data):
        if data < self.data:
            if self.left is None:
                raise ValueError("Data not in tree")
            self.left = self.left.remove_value(data)
            return self
        elif data > self.data:
            if self.right is None:
                raise ValueError("Data not in tree")
            self.right = self.right.remove_value(data)
            return self
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.data = self.right.get_min()
                self.right = self.right.remove_value(self.data)
                return self
            
    def get_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.get_min()
        
    def search_value(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.search_value(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.search_value(data)
        else:
            return True
        
    def get_tree(self):
        global list_items
        list_items.append(self.data)
        if self.left != None:
            self.left.get_tree()
        if self.right != None:
            self.right.get_tree()

    # Test code
if __name__ == "__main__":
    tree = BinarySearchTree(5)
    tree.add_values([3, 7, 1, 4, 6, 8])

    tree.remove_value(5)
    tree.remove_value(7)

    tree.search_value(5)
    tree.search_value(7)

    tree.get_tree()
    print(list_items)
