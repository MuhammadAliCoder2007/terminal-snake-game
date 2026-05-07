w = 30
l = 10
def printBoard():
    for i in range(w):
        print("-", end="")
    print()
    for i in range(l):
        print("|" + " "*(w-2)+"|")
    for i in range(w):
        print("-", end="")
    
printBoard()

