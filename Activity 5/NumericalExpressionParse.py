priorities = {
    '^' : 0,
    '*' : 1,
    '/' : 1,
    '%' : 1,
    '+' : 2,
    '-' : 2
}

def calculate(left, right, i):
    left = float(left)
    right = float(right)
    if i == '^':
        return left ** right
    elif i == '*':
        return left * right
    elif i == '/':
        return left / right
    elif i == '%':
        return left % right
    elif i == '+':
        return left + right
    elif i == '-':
        return left - right

def parse(expr):
    expr = expr.split()
    for i in priorities:
        if i in expr:
            index = expr.index(i)
            left = expr[index - 1]
            right = expr[index + 1]
            expr[index] = str(calculate(left, right, i))
            expr.pop(index + 1)
            expr.pop(index - 1)
            print(f"Current state: {' '.join(expr)}")
            return parse(' '.join(expr))


if __name__ == "__main__":
    expr = input("Enter a numerical expression (Eg: 1 + 2 * 3 / 4 ^ 5 % 6): \n")
    # expr = '2 + 3 * 5 ^ 2 - 3'
    print(f"Current state: {expr}")
    answer = parse(expr)
    # print(f"My answer: {answer}")