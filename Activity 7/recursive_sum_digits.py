def sum(n):
    if n != 0:
        return (n%10 + sum(n//10))
    else:
        return 0
    

def main():
    n = int(input("Enter a number: "))
    print(sum(n))


if __name__ == "__main__":
    main()