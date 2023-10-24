import re


def verify_brackets(brackets):
    open_brackets = 0
    close_brackets = 0

    for value in brackets.values():
        if value == '(':
            open_brackets += 1
        elif value == ')':
            close_brackets += 1

    if open_brackets == close_brackets:
        return True
    return False
    

def verify_operators(operators):
    previous_key = None
    for key in operators.keys():
        if previous_key is not None and key - previous_key == 1:
            return False
        previous_key = key
    return True


def is_valid(inp, tokens):
    # Check if the number of opening and closing brackets are equal
    bracket_flag = verify_brackets(tokens["brackets"])
    operator_flag = verify_operators(tokens["operators"])

    if not bracket_flag:
        return "Invalid Expression: Number of opening and closing brackets are not equal"
    elif not operator_flag:
        return "Invalid Expression: Adjacent operators are not allowed"
    else:
        return "Valid Expression"
    

# Tokenize the input string
def tokenize(inp):
    tokens = {
        "numbers": {},
        "operators": {},
        "brackets": {}
    }

    try:
        index = 0
        while index < len(inp):
            symbol = inp[index]

            # Check if the symbol is a number
            if re.match(r"\d", symbol):
                while index + 1 < len(inp) and re.match(r"\d", inp[index + 1]):
                    symbol += inp[index + 1]
                    index += 1
                tokens["numbers"][index] = symbol

            # Check if the symbol is an operator
            elif re.match(r"[+*/%-]", symbol):
                tokens["operators"][index] = symbol

            # Check if the symbol is a bracket
            elif re.match(r"[()]", symbol):
                tokens["brackets"][index] = symbol

            # Check if the symbol is a space
            elif re.match(r"\s", symbol):
                pass

            # If the symbol is not any of the above, it is invalid; raise an error
            else:
                raise ValueError("INVALID CHARACTER: " + symbol)
            
            index += 1
    except ValueError as e:
        print(e)
    
    return tokens


if __name__ == "__main__":
    # inp = input("Calculator expression: ")
    inp = "(2+3*(5-6) / 8) % 26"
    print("\nTokenization Result: ", )
    tokens = tokenize(inp)
    for i, j in tokens.items():
        print(f"{i}: {j}")
    
    print("\nValidation Result: ", )
    print(is_valid(inp, tokens))