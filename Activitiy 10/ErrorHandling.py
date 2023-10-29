import os


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
    
    

def do_lexical_analysis(lines):
    # Using an example as a missing semicolon at the end of the line
    exceptions = ['for', 'while', 'if', 'else', 'do', 'switch', 'case', '#include', ]
    lexical_errors = []

    print('\n')
    for line in lines:
        # Ensure that a non-comment line which is not a control statement ends with a semicolon
        if not line.startswith('//') and line[-1] != ';' and line.split()[0] not in exceptions and not 'int main()' in line and not line == '}':
            print(line)
            lexical_errors.append(f"Missing semicolon at end of line {lines.index(line) + 1}")

    return lexical_errors


def compile_time_check(lines):
    functions = [
        # (function_name, '{')
    ]

    for line in lines:
        
        
    
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

        for line, content in enumerate(lines):
            print(f"{line + 1}: {content}")

        lexical_errors = do_lexical_analysis(lines)

        if lexical_errors:
            print("\n\nLexical errors: ")
            for i in lexical_errors:
                print(i)

        # if input("\n\nDo you want to continue? (y/n): ").lower() == "n":
        #     break
        break

if __name__ == "__main__":
    main()