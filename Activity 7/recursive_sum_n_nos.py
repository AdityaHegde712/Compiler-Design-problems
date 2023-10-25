def findsum(n):
    if n == 0:
        return 0
    else:
        return n + findsum(n-1)
    

def main():
    n = int(input("Enter a number: "))
    print(findsum(n))


if __name__ == "__main__":
    main()