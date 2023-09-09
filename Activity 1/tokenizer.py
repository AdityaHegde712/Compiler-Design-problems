import re

# Regular expression patterns for identifying variables and special symbols
keyword_pattern = r'\bauto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while|main|include|stdio|stdlib|printf\b'
operator_pattern = r'[+\-*/%]|[\+\-\*/%!]=|==|!=|>=|<=|&&|\|\|\b'
variable_pattern = r'\b[a-zA-Z0-9_]+ ='
special_symbol_pattern = r'[#?\[\]]'

# Read the C file and tokenize it
file_path = 'Activity 1\\test.c'
with open(file_path, 'r') as file:
    content = file.read()


keywords = list(set(re.findall(keyword_pattern, content)))
operators = list(set(re.findall(operator_pattern, content)))
variables = list(set(re.findall(variable_pattern, content)))
specials = list(set(re.findall(special_symbol_pattern, content)))

print(f"Keywords: {' '.join(keywords)}")
print(f"Operators: {' '.join(operators)}")
print(f"Variables: {' '.join(variables)}")
print(f"Special Symbols: {' '.join(specials)}")