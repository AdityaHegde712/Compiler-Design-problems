import os
import re

start = "\n----------------------------------------\n"

def read_file(fname):
    try:
        with open(fname, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        return None
    

def preprocess_content(content):
    lines = [i.strip() for i in content.split("\n") if i.strip() != ""]
    lines = [i for i in lines if not i.startswith("//")]
    lines = [i for i in lines if not i.startswith("/*")]
    lines = [i for i in lines if not i.startswith("*/")]

    lines = [line.split('//')[0].strip() for line in lines]

    return lines
    
    

def lexical_analysis(lines):
    # Using an example as a missing semicolon at the end of the line
    exceptions = ['for', 'while', 'if', 'else', 'do', 'switch', 'case', '#include', ]
    lexical_errors = []

    for line in lines:
        # Ensure that a non-comment line which is not a control statement ends with a semicolon
        if not line.startswith('//') and line[-1] != ';' and line.split()[0] not in exceptions and not 'int main()' in line and not line == '}':
            lexical_errors.append(f"Missing semicolon at end of line {lines.index(line) + 1}")

    if lexical_errors:
        print(f"{start}Lexical errors: ")
        for i in lexical_errors:
            print(i)


def compile_time_check(lines):
    functions = [
        # (function_name, line_num)
    ]

    # Check if all curly braces are closed. For each open curly brace, append tuple of line and line number to 'functions'. For each closed brace, pop the last element from 'functions'
    for line in lines:
        if re.match(r'[\[\]a-zA-Z0-9 =,;]*{[\[\]a-zA-Z0-9 =,;]*}[\[\]a-zA-Z0-9 =,;]*', line):
            pass
        elif line == '{':
            functions.append((lines[lines.index(line) - 1], lines.index(line) + 1))
        elif '{' in line:
            functions.append((line.split('{')[0], lines.index(line) + 1))
        elif '}' in line:
            functions.pop()
    
    # If functions is not empty, print error
    if functions:
        print(f"{start}Syntactical errors: ")
        print("Missing closing curly brace for function(s): ")
        for function in functions:
            print(f"{function[0]} at line {function[1]}")


def show_runtime_error():
    print(f"{start}Runtime errors: ")
    try:
        string = 'a = 1 / 0'
        a = 1 / 0
    except Exception as e:
        print(f"{e} at line: {string}")

    try:
        string = 'print([1, 2, 3][3])'
        print([1, 2, 3][3])
    except Exception as e:
        print(f"{e} at line: {string}")

    try:
        print(1 + "2")
    except Exception as e:
        print(e)

    try:
        print(a)
    except Exception as e:
        print(e)


def show_logical_error():
    error = f"""{start}A compiler cannot detect logical errors in a program. It can only detect syntactical errors. For example, the following code will not give any errors, but it is logically incorrect:
int a = 1;
int b = 2;
int c = a + b;
print(c)

The above code will print 3, but it is logically incorrect. The correct code should be:

int a = 1;
int b = 2;
int c = a * b;
print(c)
The above code will print 2, which is the correct answer. However, the compiler cannot detect this error. It can only detect syntactical errors, such as missing semicolons, missing curly braces, etc.
          """
    print(error)


def main():
    # Print present working directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    while True:
        # fname = input("Enter filename: ")
        fname = 'sample.c'
        if fname == "exit":
            break
        content = read_file(fname)
        
        lines = preprocess_content(content)

        print(f"{start}Raw uncommented unindented code: ")
        for line, content in enumerate(lines):
            print(f"{line + 1}: {content}")

        # Do the checks
        lexical_analysis(lines)
        compile_time_check(lines)
        show_runtime_error()
        show_logical_error()


        # if input("\n\nDo you want to continue? (y/n): ").lower() == "n":
        #     break
        break

if __name__ == "__main__":
    main()