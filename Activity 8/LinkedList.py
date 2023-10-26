# Implement a class for a singly linked list
# The class should have a method for adding a node to the end of the list
# The class should have a method for adding a node to a specific position in the list
# The class should have a method for removing a node from the list
# The class should have a method to search for a value through the list
list_items = []


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
        global list_items
        list_items.append(self.data)
        if self.next != None:
            self.next.get_list()
        

if __name__ == '__main__':
    
    # Test cases
    # Create a linked list with 3 nodes
    linked_list = LinkedList(1)
    linked_list.append_node(2)
    linked_list.append_node(3)
    linked_list.append_node(4)
    linked_list.append_node(5)

    # Insert a node at the beginning of the list
    linked_list = linked_list.insert_node(0, 0)

    # Insert a node at the end of the list
    linked_list = linked_list.insert_node(6, 6)

    # Insert a node in the middle of the list
    linked_list = linked_list.insert_node(3.5, 4)

    # Remove a node from the list
    linked_list = linked_list.remove_node(4)

    # Search for a node in the list
    print(linked_list.search_node(3.5))

    # Print the list
    linked_list.get_list()
    print(list_items)