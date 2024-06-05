def asterisks(b, a):  
    if b < (a + 1):  
        print("*" * b)

        asterisks(b + 1, a)
    else:
        return 0

def main():
    n = int(input("Enter an integer: "))
    asterisks(1, n)


main()