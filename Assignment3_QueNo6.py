from sys import getsizeof

def getInfo(Variable):
    print("Data Type of variable is :",type(Variable))
    print("Memory Address of variable is:",id(Variable))
    print("Size in Bytes is: ",getsizeof(Variable))

def main():
    print("Please type something:")
    A=input()
    getInfo(A)

if __name__ == "__main__":
    main()