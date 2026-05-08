w = 30
l = 10

snake = [(15, 5)]

def printChar(char):
    print(char)
def printBoard():
    
    for i in range(w):
        print("-", end="")
    print()
    for i in range(l):
        print("|" + " "*(w-2)+"|")
        if i==5:
            printChar("\tOOOX")
    for i in range(w):
        print("-", end="")


printBoard()


