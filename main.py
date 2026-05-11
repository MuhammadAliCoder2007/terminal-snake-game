w = 30
l = 10

snake = [(15, 5)]


def printBoard():
    
    for row in range(l):
        line = ""
        for col in range(w):
            if (col, row) in snake:
                line += "O"
printBoard()


