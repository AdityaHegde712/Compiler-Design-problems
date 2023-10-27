from InputData import input_processes, input_memory_blocks
from SourceMethods import first_fit, best_fit, worst_fit, next_fit, get_waste


def do_fit(processes, memory_blocks, type):
    if type == 'first_fit':
        used_blocks, remaining_memory_blocks, bad_processes = first_fit(processes, memory_blocks)
    elif type == 'best_fit':
        used_blocks, remaining_memory_blocks, bad_processes = best_fit(processes, memory_blocks)
    elif type == 'worst_fit':
        used_blocks, remaining_memory_blocks, bad_processes = worst_fit(processes, memory_blocks)
    elif type == 'next_fit':
        used_blocks, remaining_memory_blocks, bad_processes = next_fit(processes, memory_blocks)

    waste = get_waste(processes, used_blocks)
    print(f"\nUsed blocks: {used_blocks}")
    print(f"\nUnused memory blocks: {remaining_memory_blocks}")
    print(f"\nUnallocated processes: {bad_processes}")
    print(f"\nTotal wasted space: {waste}")


def main():
    while True:
        print("\nProcess input: ")
        processes = input_processes()
        print(f"\nGiven Processes: \n{processes}")

        print("\nMemory block input: ")
        memory_blocks = input_memory_blocks()
        print(f"\nGiven Memory Blocks: \n{memory_blocks}")

        print("\n----------------------------------------------------------------------\nFirst fit: ")
        print(f"\nGiven Processes: \n{processes}")
        print(f"\nGiven Memory Blocks: \n{memory_blocks}")
        do_fit(processes, memory_blocks, type='first_fit')

        print("\n----------------------------------------------------------------------\nBest fit: ")
        print(f"\nGiven Processes: \n{processes}")
        print(f"\nGiven Memory Blocks: \n{memory_blocks}")
        do_fit(processes, memory_blocks, type='best_fit')

        print("\n----------------------------------------------------------------------\nWorst fit: ")
        print(f"\nGiven Processes: \n{processes}")
        print(f"\nGiven Memory Blocks: \n{memory_blocks}")
        do_fit(processes, memory_blocks, type='worst_fit')

        print("\n----------------------------------------------------------------------\nNext fit: ")
        print(f"\nGiven Processes: \n{processes}")
        print(f"\nGiven Memory Blocks: \n{memory_blocks}")
        do_fit(processes, memory_blocks, type='next_fit')

        if input("\n\nDo you want to continue? (y/n): ").lower() == "n":
            break


if __name__ == "__main__":
    main()