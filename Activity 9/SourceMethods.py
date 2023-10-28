def first_fit(processes, memory_blocks): 
    used_blocks = []
    bad_processes = []
    memory_blocks_copy = memory_blocks.copy() # Create a copy of the memory_blocks list
    for process in processes:
        for block in memory_blocks: # Iterate over the copy of the memory_blocks list
            if block[1] >= process[1] and block[1] not in [used_block[1] for used_block in used_blocks]:
                print(f"{process[0]} is allocated to {block[0]}")
                used_blocks.append(list(memory_blocks_copy.pop(memory_blocks_copy.index(block))) + [process[0]])
                break
        else:
            print(f"{process[0]} is not allocated to any memory block")
            bad_processes.append(process)

    memory_blocks_copy = [block for block in memory_blocks_copy if block[0] not in used_blocks]

    return used_blocks, memory_blocks_copy, bad_processes
    # used_blocks = []
    # bad_processes = []
    # for process in processes:
    #     allocated = False
    #     for block in memory_blocks:
    #         if block[1] >= process[1] and block[1] not in [used_block[1] for used_block in used_blocks]:
    #             used_blocks.append(list(block) + [process[0]])
    #             allocated = True
    #             break
    #     if not allocated:
    #         bad_processes.append(process)
            
    #         print(f"{process[0]} is not allocated to any memory block")

    #     else:
    #         print(f"{process[0]} is allocated to {block[0]}")

    # memory_blocks = [block for block in memory_blocks if block not in used_blocks]

    # return used_blocks, memory_blocks, bad_processes


def best_fit(processes, memory_blocks):
    bad_processes = []
    used_blocks = []
    memory_blocks_copy = memory_blocks.copy() # Create a copy of the memory_blocks list
    for process in processes: # Iterate through processes
        best_block = None
        for block in memory_blocks: # Iterate through memory blocks for each process
            if block[1] >= process[1] and block[1] not in [used_block[1] for used_block in used_blocks]:
                if best_block is None:
                    best_block = block
                elif block[1] < best_block[1]:
                    best_block = block
        if best_block is not None:
            print(f"{process[0]} is allocated to {best_block[0]}")

            used_blocks.append(list(memory_blocks_copy.pop(memory_blocks_copy.index(best_block))) + [process[0]])
        else:
            print(f"{process[0]} is not allocated to any memory block")
            bad_processes.append(process)

    return used_blocks, memory_blocks_copy, bad_processes # Return used blocks, unused blocks, unallocated processes


def worst_fit(processes, memory_blocks):
    used_blocks = []
    bad_processes = []
    memory_blocks_copy = memory_blocks.copy()
    for process in processes: # Iterate through processes
        worst_block = None
        for block in memory_blocks: # Iterate through memory blocks for each process
            if block[1] >= process[1] and block[1] not in [used_block[1] for used_block in used_blocks]:
                if worst_block is None:
                    worst_block = block
                elif block[1] > worst_block[1]:
                    worst_block = block
        if worst_block is not None:
            print(f"{process[0]} is allocated to {worst_block[0]}")

            used_blocks.append(list(memory_blocks_copy.pop(memory_blocks_copy.index(worst_block))) + [process[0]])
        else:
            print(f"{process[0]} is not allocated to any memory block")
            bad_processes.append(process)

    return used_blocks, memory_blocks_copy, bad_processes # Return used blocks, unused blocks, unallocated processes


def next_fit(processes, memory_blocks):
    used_blocks = []
    bad_processes = []
    memory_blocks_copy = memory_blocks.copy() # Create a copy of the memory_blocks list
    for process in processes:
        for i in range(len(memory_blocks)): # Iterate over the copy of the memory_blocks list
            block = memory_blocks[i]
            if block[1] >= process[1] and block[1] not in [used_block[1] for used_block in used_blocks]:
                print(f"{process[0]} is allocated to {block[0]}")
                used_blocks.append(list(memory_blocks_copy.pop(memory_blocks_copy.index(block))) + [process[0]])
                # i is now the next block after the one currently appended
                memory_blocks = memory_blocks[i:]
                break
        else:
            print(f"{process[0]} is not allocated to any memory block")
            bad_processes.append(process)

    return used_blocks, memory_blocks_copy, bad_processes

def get_waste(processes, used_blocks):
    total_waste = []
    for process in processes:
        for block in used_blocks:
            if process[0] == block[2]:
                total_waste.append([block[1] - process[1], process[0]])
    return total_waste