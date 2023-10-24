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

# Example postfix expression
postfix_expression = "abcd-*e/+h%"
ast = build_ast_from_postfix(postfix_expression)

# Create a code generator and generate 3-address code
code_generator = ThreeAddressCodeGenerator()
result = code_generator.generate_3addr_code(ast)
