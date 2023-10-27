
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append_node(self, data):
        if self.next == None:
            self.next = LinkedList(data)
        else:
            self.next.append_node(data)
    
    def append_nodes(self, dataList):
        for data in dataList:
            self.append_node(data)
        return self

    def insert_node(self, data, position):
        if position == 0:
            new_node = LinkedList(data)
            new_node.next = self
            return new_node

        elif position == 1:
            new_node = LinkedList(data)
            new_node.next = self.next
            self.next = new_node
            return self

        else:
            if self.next is None:
                raise ValueError("Position out of range")
            self.next = self.next.insert_node(data, position - 1)
            return self
        
    def remove_node(self, data):
        if self.data == data:
            return self.next
        else:
            if self.next is None:
                raise ValueError("Data not in list")
            self.next = self.next.remove_node(data)
            return self
        
    def search_node(self, data):
        if self.data == data:
            return True
        else:
            if self.next is None:
                return False
            return self.next.search_node(data)
        
    def get_list(self):
        print(self.data, end=", ")
        if self.next != None:
            self.next.get_list()


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
        print(self.data, end=", ")
        if self.left != None:
            self.left.get_tree()
        if self.right != None:
            self.right.get_tree()


from HashMap import HashMap
from Array import Array
from random import randint
from time import time

if __name__ == "__main__":
    print("\nTHIS IS THE DATA STRUCTURE COMPARATIVE STUDY")
    print("The available data structures are LinkedLists, Binary Search Trees, Hash Maps, and Arrays.")
    size = int(input("\nPlease input the size of these data structures: "))
    items = set()
    while len(items) < size:
        items.add(randint(0, size*2))
    items = list(items)

    print("\nCreating Data Structures...")
    linked_list = LinkedList(items[0])
    linked_list.append_nodes(items[1:])

    binary_search_tree = BinarySearchTree(items[0])
    binary_search_tree.add_values(items[1:])

    hash_map = HashMap()
    hash_map.add_values(items)

    array = Array(items)
    print("Done!")

    while True:
        choice = int(input("""\nNext, please enter a function you would like to benchmark for each of the data structures:
1. Insert (at beginning)
2. Search
3. Remove
4. Print
5. Exit

Choice: """))
        
        if choice == 1:
            ele = int(input("Please enter the element you would like to insert: "))
            print("Benchmarking...")
            start = time()
            linked_list = linked_list.insert_node(ele, 0)
            end = time()
            print(f"Linked List: {end - start}")

            start = time()
            binary_search_tree.add_value(ele)
            end = time()
            print(f"Binary Search Tree: {end - start}")

            start = time()
            hash_map.add_value(ele)
            end = time()
            print(f"Hash Map: {end - start}")

            start = time()
            array.insert_value(ele)
            end = time()
            print(f"Array: {end - start}")

        elif choice == 2:
            ele = int(input("Please enter the element you would like to search for: "))
            print("Benchmarking...")
            start = time()
            linked_list.search_node(ele)
            end = time()
            print(f"Linked List: {end - start}")

            start = time()
            binary_search_tree.search_value(ele)
            end = time()
            print(f"Binary Search Tree: {end - start}")

            start = time()
            hash_map.search_value(ele)
            end = time()
            print(f"Hash Map: {end - start}")

            start = time()
            array.search_value(ele)
            end = time()
            print(f"Array: {end - start}")

        elif choice == 3:
            ele = int(input("Please enter the element you would like to remove: "))
            print("Benchmarking...")
            start = time()
            linked_list = linked_list.remove_node(ele)
            end = time()
            print(f"Linked List: {end - start}")

            start = time()
            binary_search_tree.remove_value(ele)
            end = time()
            print(f"Binary Search Tree: {end - start}")

            start = time()
            hash_map.remove_value(ele)
            end = time()
            print(f"Hash Map: {end - start}")

            start = time()
            array.remove_value(ele)
            end = time()
            print(f"Array: {end - start}")

        elif choice == 4:
            print("\nThe data structures currently are:")
            print(f"Linked List: ")
            linked_list.get_list()
            print("None")

            print(f"Binary Search Tree: ")
            binary_search_tree.get_tree()
            print("End")

            hash_map.print_hash_map_readable()
            array.print_array()

        else:
            exit(1)