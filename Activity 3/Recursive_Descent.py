# Implement recursive descent parser for the following grammar:
# E -> TE'
# E' -> +TE' | epsilon
# T -> FT'
# T' -> *FT' | epsilon
# F -> (E) | id

def E():
    T()
    Eprime()

def Eprime():
    global i  # Add this line to indicate that you want to modify the global 'i' variable
    if i < len(s) and s[i] == '+':
        i += 1
        T()
        Eprime()

def T():
    F()
    Tprime()

def Tprime():
    global i  # Add this line to indicate that you want to modify the global 'i' variable
    if i < len(s) and s[i] == '*':
        i += 1
        F()
        Tprime()

def F():
    global i  # Add this line to indicate that you want to modify the global 'i' variable
    if i < len(s):
        if s[i] == '(':
            i += 1
            E()
            if i < len(s) and s[i] == ')':
                i += 1
            else:
                print("Error: Expected closing parenthesis")
        elif s[i] == 'i' and i+1 < len(s) and s[i+1] == 'd':
            i += 2  # Consume 'id' as a whole
        else:
            print("Error: Invalid input")

s = input("Enter a string: ")  # Test string: id+id*id$
i = 0
E()
if i == len(s):
    print("Valid")
else:
    print("Invalid")
