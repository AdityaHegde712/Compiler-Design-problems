import re
from infixToPostfix import Conversion

class Node:
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class OperatorNode(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class ThreeAddressCodeGenerator:
    def __init__(self):
        self.temp_counter = 1

    def get_temp_var(self):
        temp_var = f'T{self.temp_counter}'
        self.temp_counter += 1
        return temp_var

    def generate_3addr_code(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, OperatorNode):
            left_operand = self.generate_3addr_code(node.left)
            right_operand = self.generate_3addr_code(node.right)
            result_temp = self.get_temp_var()
            operator = node.operator
            print(f"{result_temp} = {left_operand} {operator} {right_operand}")
            return result_temp
        else:
            print("Invalid node found")
            print(type(node))
            

def build_ast_from_postfix(postfix_expression):
    stack = []
    operators = set('+-*/%')

    for token in postfix_expression:
        if token.isalpha():
            stack.append(NumberNode(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            right = stack.pop()
            left = stack.pop()
            stack.append(OperatorNode(token, left, right))
        else:
            raise ValueError("Invalid token in postfix expression: " + token)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack[0]  # The top of the stack is the root of the AST


def print_ast(node, level=0):
    if isinstance(node, NumberNode):
        print(f"{'  |' * level}Number: {node.value}")
    elif isinstance(node, OperatorNode):
        print(f"{'  |' * level}Operator: {node.operator}")
        print_ast(node.left, level + 1)
        print_ast(node.right, level + 1)


def verify_brackets(inp):
    count = 0
    for i in inp:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
    

def verify_operators(inp):
    for i in range(len(inp) - 1):
        if inp[i] in ['+', '-', '*', '/', '%'] and inp[i + 1] in ['+', '-', '*', '/', '%']:
            return False
    return True


def is_valid(inp):
    # Check if the number of opening and closing brackets are equal
    bracket_flag = verify_brackets(inp)
    operator_flag = verify_operators(inp)

    if not bracket_flag:
        return "Invalid Expression: Number of opening and closing brackets are not equal"
    elif not operator_flag:
        return "Invalid Expression: Adjacent operators are not allowed"
    else:
        return "Valid Expression"
    

# Tokenize the input string
def tokenize(inp):
    tokens = [
        # list of tuples, each (symbol, class)
    ]

    try:
        index = 0
        while index < len(inp):
            symbol = inp[index]

            # Check if the symbol is a number
            if re.match(r"[a-zA-Z]", symbol):
                tokens.append((symbol, "variable"))

            # Check if the symbol is an operator
            elif re.match(r"[+*/%-]", symbol):
                tokens.append((symbol, "operator"))

            # Check if the symbol is a bracket
            elif re.match(r"[()]", symbol):
                tokens.append((symbol, "bracket"))

            # If the symbol is not any of the above, it is invalid; raise an error
            else:
                raise ValueError("INVALID CHARACTER: " + symbol)
            
            index += 1
    except ValueError as e:
        print(e)
    
    return tokens


# Remove spaces from the input string
def remove_spaces(inp):
    return inp.replace(" ", "")


if __name__ == "__main__":
    # inp = remove_spaces(input("Calculator expression: "))
    inp = remove_spaces("(a+b*(c-d) / e) % h")
    print("\nInput: ", inp)
    
    print("\nTokenization Result: ", )
    tokens = tokenize(inp)
    print(tokens)
    
    print("\nValidation Result: ", )
    print(is_valid(inp))

    print("\nAfter converting to postfix:")
    inp = Conversion(len(inp)).infixToPostfix(inp)
    print(inp)

    print("\nAST:")
    ast = build_ast_from_postfix(inp)
    print_ast(ast)

    print("\nThree Address Code:")
    ThreeAddressCodeGenerator().generate_3addr_code(ast)
