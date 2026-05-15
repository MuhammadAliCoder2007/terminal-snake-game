import random


w = 30
l = 10

snake = []
food = []
dx,dy = 0,0

fx = random.randint(1,w-2)
fy = random.randint(1,l-2)
def printBoard(): 
    for row in range(l):
        line = ""
        for col in range(w):
            if (col, row) in snake:
                line += "O"
            elif (col,row) == food:
                line+= "*"
            elif row==0 or row==l-1:
                line+= "-"
            elif col ==0 or col==w-1:
                line+= "|"
            else:
                line+= " "
        print(line)
def move():
    global snake, dx, dy,food
    head_x, head_y = snake[0]
    snake = [(head_x + dx, head_y + dy)] + snake[:-1]

def newFood():
    while True:
        fx = random.randint(1,w-2)
        fy = random.randint(1,l-2)
        if (fx,fy) not in snake:
            return (fx,fy)


def game():
    global snake, dx, dy,food
    food = newFood()
    snake = [(15,5)]
    dx, dy = 0,0

    while True:
        printBoard()
        dx = 0
        dy = 0
        key = input("Move (wasd): ").strip().lower()
        if key == 'w':
            dx,dy= 0,-1
        elif key == 'a':
            dx , dy= -1,0
        elif key == 'd':
            dx,dy = 1,0
        elif key == 's':
            dx,dy = 0,1
        else:
            print("Invalid Input")
            continue
        move()
        hx,hy = snake[0]
        if snake[0]==food[0]:
            food = newFood()

        if hx==0 or hx==w-1 or hy==0 or hy==l-1:
            print("Game Over")
            break
game()
        




