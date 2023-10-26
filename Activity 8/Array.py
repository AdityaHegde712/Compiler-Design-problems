import array

# Create a class called Array that has a constructor that takes a list of numbers as a parameter.
# The class should have a method that inserts a value into the array.
# The class should have a method that removes a value from the array.
# The class should have a method that searches for a value in the array.
# The class should have a method that prints the array.

class Array:
    def __init__(self, data):
        self.array = array.array('i', data)

    def insert_value(self, data):
        self.array.append(data)

    def remove_value(self, data):
        self.array.remove(data)

    def search_value(self, data):
        if data in self.array:
            return True
        return False
    
    def print_array(self):
        print(self.array)

# Test your class by creating an array, adding values, searching for values, removing values, and printing the array.
if __name__ == "__main__":
    my_array = Array([1,2,3,4,5])
    my_array.print_array()
    my_array.insert_value(6)
    my_array.print_array()
    my_array.remove_value(3)
    my_array.print_array()
    print(my_array.search_value(3))
    print(my_array.search_value(4))