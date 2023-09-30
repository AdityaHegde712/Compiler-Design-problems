def read():
    with open('Activity 4\CFG.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def split(cfg):
    return [line.replace(' ', '') for line in cfg]


def bad_firsts(bad, cfg):
    for i in cfg:
        if i.startswith(bad) and i[3].islower():
            return i[3]
        elif i.startswith(bad) and i[3].isupper():
            return bad_firsts(i[3], cfg)


def get_firsts(cfg):
    non_terminals = []
    firsts = []

    # Get non-terminals
    for line in cfg:
        non_terminals.append(line[0])
    
    # Compute firsts
    for line in cfg:
        if line[3].islower():
            firsts.append(line[3])
        else:
            firsts.append(bad_firsts(line[3], cfg))
    return dict(zip(non_terminals, firsts))


def bad_follow(bad, cfg):
    pass


def get_follows(cfg, firsts, non_terminals):
    productions = []
    follows = {}
    # Get productions
    for line in cfg:
        productions.append(line[3:])
    
    # Compute follows
    for non_terminal in non_terminals: # Find the follow for each non-terminal
        follows[non_terminal] = []

        # Add $ to follow of first non-terminal
        if non_terminal == non_terminals[0]:
            follows[non_terminal].append('$')
        
        # Main follow computation
        for production, line in zip(productions, cfg): # Iterate through each production
            if non_terminal in production: 
                if not non_terminal == production[-1]: # If the non-terminal is not the last character in the production
                    if production[production.index(non_terminal) + 1].islower():
                        follows[non_terminal].append(production[production.index(non_terminal) + 1])
                    else:
                        follows[non_terminal].append(firsts[production[production.index(non_terminal) + 1]])
                elif not non_terminal == line[0]: # If this is the production for a non-terminal that is not the current non-terminal
                    follows[non_terminal] += follows[line[0]] # Save this for your rubber duck programming moment
                else: 
                    pass # If the non-terminal is the last character in its own production, do nothing

    return follows


def construct_parsing_table(grammar, firsts, follows, non_terminals):
    parsing_table = {}

    # Initialize the parsing table
    for non_terminal in non_terminals:
        parsing_table[non_terminal] = {}

    print(parsing_table)

    for production in grammar:
        left, right = production.split('->')
        right = right.strip()
        first_of_right = first_of_string(right, firsts)

        for symbol in first_of_right:
            if symbol != 'ε':
                parsing_table[left][symbol] = production

        if 'ε' in first_of_right:
            for follow_symbol in follows[left]:
                parsing_table[left][follow_symbol] = production

    return parsing_table


def first_of_string(s, firsts):
    first_set = set()
    for symbol in s:
        if symbol in firsts.keys():
            first_set.update(firsts[symbol])
            if 'ε' not in firsts[symbol]:
                break
    return first_set


if __name__ == '__main__':
    cfg = read()
    cfg = split(cfg)
    firsts = get_firsts(cfg)
    non_terminals = list(firsts.keys())
    follows = get_follows(cfg, firsts, non_terminals)

    print(f"Split CFG: \n{cfg}")
    print(f"\nFirsts: \n{firsts}")
    print(f"\nFollows: \n{follows}\n")


    parsing_table = construct_parsing_table(cfg, firsts, follows, non_terminals)
    print(parsing_table)