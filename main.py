w = 30
l = 10

snake = [(15, 5)]


def printBoard(): 
    for row in range(l):
        line = ""
        for col in range(w):
            if (col, row) in snake:
                line += "O"
            elif row==0 or row==l-1:
                line+= "-"
            elif col ==0 or col==w-1:
                line+= "|"
            else:
                line+= " "
        print(line)
def move():
    global snake, dx, dy
    head_x, head_y = snake[0]
    snake = [(head_x + dx, head_y + dy)] + snake[:-1]


while True:
    printBoard()

    key = input("Move (wasd): ").strip().lower()

    if key == 'w':
        dx,dy= 0,-1
    elif key == 'a':
        dx , dy= -1,0
    elif key == 'd':
        dx,dy = 1,0
        dy = 0
    elif key == 's':
        dx,dy = 0,1
    move()



