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


def get_follows(cfg, firsts, non_terminals):
    productions = []
    follows = []
    # Get productions
    for line in cfg:
        productions.append(line[3:])
    
    # Compute follows
    for non_terminal in non_terminals: # Find the follow for each non-terminal
        follow = []

        # Add $ to follow of first non-terminal
        if non_terminal == non_terminals[0]:
            follow.append('$')
        
        # Main follow computation
        for production in productions: # Iterate through each production
            if non_terminal in production: 
                if not non_terminal == production[-1]: # If the non-terminal is not the last character in the production
                    if production[production.index(non_terminal) + 1].islower():
                        follow.append(production[production.index(non_terminal) + 1])
                    else:
                        follow.append(firsts[production[production.index(non_terminal) + 1]])
                elif not non_terminal == production[0]: # If this is the production for a non-terminal that is not the current non-terminal
                    pass # Save this for your rubber duck programming moment
                # You are at the point where you're checking for the follows of the non-terminal when it's last, and the current production does not belong to the current non-terminal
                # THE FLAW IN THIS CODE IS THAT THE PRODUCTION DOES NOT CONTAIN THE RESPECTIVE NON-TERMINAL
                # I WILL NEED TO CHANGE IT FROM ITERATING THROUGH THEM SEPARATELY TO ITERATING THROUGH THE LINES OF THE CFG ITSELF WITHOUT SPLITTING IT
                # AAAAAAAAAAAAAAAAAAAAAAA EUREKA BUT I NEED TO SLEEP
                # I WILL CONTINUE TOMORROW
                # I WILL CONTINUE TOMORROW
                # I WILL CONTINUE TOMORROW
                # GOOD JOB ME


if __name__ == '__main__':
    cfg = read()
    cfg = split(cfg)
    firsts = get_firsts(cfg)
    non_terminals = list(firsts.keys())
    follows = get_follows(cfg, firsts, non_terminals)

    print(f"Split CFG: \n{cfg}")
    print(f"\nFirsts: \n{firsts}")
    print(f"\nFollows: \n{follows}")