import re





# Tokenize the input string
def tokenize(inp):
    tokens = {
        "numbers": {},
        "operators": {},
        "brackets": {}
    }

    try:
        for index, symbol in enumerate(inp):
            # Check if the symbol is a number
            if re.match(r"\d", symbol):
                while True:
                    if re.match(r"\d", inp[index + 1]):
                        symbol += inp[index + 1]
                        index += 1
                    else:
                        break
                print(symbol)
            # Check if the symbol is an operator
            elif re.match(r"[+*/%-]", symbol):
                tokens["operators"][index] = symbol

            # Check if the symbol is a bracket
            elif re.match(r"[()]", symbol):
                tokens["brackets"][index] = symbol

            # Check if the symbol is a space
            elif re.match(r"\s", symbol):
                continue

            # If the symbol is not any of the above, it is invalid; raise an error
            else:
                raise ValueError("INVALID CHARACTER: " + symbol)
            
            print(symbol)
    except ValueError as e:
        print(e)
    
    return tokens


if __name__ == "__main__":
    # inp = input("Calculator expression: ")
    inp = "(2+3*(5-6) / 8) % 26"
    tokens = tokenize(inp)
    print("Tokenization Result: ", )
    
    for token_type in tokens:
        print(token_type + ": ", end="")
        for token in tokens[token_type]:
            print(tokens[token_type][token], end=" ")
        print()