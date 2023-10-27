def input_processes():
    processes = []
    counter = 0
    while True:
        try:
            process = int(input("Enter the size of process (enter 0 to stop): "))
            if process == 0:
                break
            processes.append((f"P{counter}", process))
            counter += 1
        except ValueError:
            print("Please enter a valid number!")
    return processes


def input_memory_blocks():
    memory_blocks = []
    counter = 0
    while True:
        try:
            block = int(input("Enter the size of the memory block (enter 0 to stop): "))
            if block == 0:
                break
            memory_blocks.append((f"M{counter}", block))
            counter += 1
        except ValueError:
            print("Please enter a valid number!")
    return memory_blocks