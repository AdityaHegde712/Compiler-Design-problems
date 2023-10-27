# Define a class to manually create a hash map, with a hash function. Each key is a number, from 0 to 26, and each value is a list of integers. 
# The hash function should take a number and return a number between 0 and 26.
# The class should have a method to add a value to the hash map, using the hash function to determine the key.
# The class should have a method to search for a value in the hash map, using the hash function to determine the key.
# The class should have a method to remove a value from the hash map, using the hash function to determine the key.
# The class should have a method to print the hash map.
# The class should have a method to print the hash map in a readable format.

class HashMap:
    def __init__(self):
        self.hash_map = {}
        for i in range(27):
            self.hash_map[i] = []

    def hash_function(self, data):
        return (data * 12) % 27
    
    def add_value(self, data):
        key = self.hash_function(data)
        self.hash_map[key].append(data)

    def add_values(self, dataList):
        for data in dataList:
            self.add_value(data)
        return self

    def search_value(self, data):
        key = self.hash_function(data)
        if data in self.hash_map[key]:
            return True
        return False
    
    def remove_value(self, data):
        key = self.hash_function(data)
        if data in self.hash_map[key]:
            self.hash_map[key].remove(data)
            return True
        return False
    
    def print_hash_map(self):
        print(self.hash_map)

    def print_hash_map_readable(self):
        for key in self.hash_map:
            print(f"{key}: {self.hash_map[key]}")

# Test your class by creating a hash map, adding values, searching for values, removing values, and printing the hash map.
if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.add_values(list(range(0,27)))
    hash_map.print_hash_map_readable()
    hash_map.remove_value(13)
    hash_map.print_hash_map_readable()