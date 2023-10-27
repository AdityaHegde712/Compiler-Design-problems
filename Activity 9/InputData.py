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
    # return [('P0', 20), ('P1', 50), ('P2', 100), ('P3', 500), ('P4', 100)]


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
    # return [('M0', 100), ('M1', 200), ('M2', 500), ('M3', 300), ('M4', 600), ('M5', 800), ('M6', 20), ('M7', 60), ('M8', 250)]