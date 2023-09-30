from random import randint

def read_sets(num_sets):
    sets = []
    for _ in range(num_sets):
        sets.append(set(input("Enter the numbers with spaces in between (Eg: 1 2 3 4 5): \n").split()))
    return sets


def gen_sets(num_sets):
    sets = []
    for _ in range(num_sets):
        sets.append(set([str(randint(1, 100)) for _ in range(randint(1, 10))]))
    return sets


def find_min(set):
    min = float('inf')
    for i in set:
        if int(i) < min:
            min = int(i)
    return min


def init_table(no_keys):
    table = {}
    for i in range(no_keys):
        table[i] = []
    return table


def make_table(no_keys, sets):
    table = init_table(no_keys)
    for set in sets:
        h_val = find_min(set) % no_keys
        table[h_val].append(set)
    return table


if __name__ == '__main__':
    # sets = read_sets(int(input("Enter the number of sets: \n")))
    sets = gen_sets(int(input("Enter the number of sets: \n")))
    no_keys = int(input("Enter the number of keys: \n"))

    # Printing the sets
    counter = 1
    for set in sets:
        print(f"Set {counter}: {set}")
        counter += 1

    print('\n')
    inverse_table = make_table(no_keys, sets)
    for key, value in inverse_table.items():
        print(f"Hash value {key}: {value}")
