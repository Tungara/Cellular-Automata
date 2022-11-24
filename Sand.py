import pygame
import random
pygame.init()


def makeGrid(rows, columns):
    Matrix = [[0 for x in range(rows)] for y in range(columns)]

    for object in Matrix:
        for i in range(len(object)):
            object[i] = 0

    for i in range(rows):
        Matrix[i][rows-1] = 2


    return Matrix


def updateWin():
    global Size, Matrix, window, height

    # Sets the pixels
    pixel_size = width / Size
    for i in range(Size):
        for j in range(Size):
            if Matrix[i][j] == 0:
                pygame.draw.rect(window, (0, 0, 0), pygame.Rect(pixel_size*i, pixel_size*j, pixel_size, pixel_size))
            elif Matrix[i][j] == 1:
                pygame.draw.rect(window, (242, 209, 107), pygame.Rect(pixel_size*i, pixel_size*j, pixel_size, pixel_size))
            elif Matrix[i][j] == 2:
                pygame.draw.rect(window, (0, 0, 0), pygame.Rect(pixel_size*i, pixel_size*j, pixel_size, pixel_size))

    # draws grid lines
    for line in range(Size):
        pygame.draw.line(window, (116, 116, 116), (0, line * width/Size), (width, line * width/Size))
        pygame.draw.line(window, (116, 116, 116), (line * height/Size, 0), (line * height/Size, height))

    for i in range(Size):
        Matrix[i][Size-1] = 2

    pygame.display.update()


def moveCells():
    global Matrix
    MatrixNewGen = makeGrid(Size, Size)
    for i in range(Size):
        for j in range(Size):
            try:
                surroundingCells = [Matrix[i][j+1], Matrix[i+1][j+1], Matrix[i-1][j+1]]
                if Matrix[i][j] == 1:
                    if surroundingCells[0] == 0:
                        MatrixNewGen[i][j+1] = 1
                        MatrixNewGen[i][j] = 0
                    else:
                        if surroundingCells[1] == 0 and surroundingCells[2] == 0:
                            choice = random.randint(0, 1)
                            if choice == 1:
                                MatrixNewGen[i+1][j+1] = 1
                                MatrixNewGen[i][j] = 0
                            elif choice == 0:
                                MatrixNewGen[i-1][j + 1] = 1
                                MatrixNewGen[i][j] = 0
                        elif surroundingCells[1] == 0:
                            MatrixNewGen[i + 1][j + 1] = 1
                            MatrixNewGen[i][j] = 0
                        elif surroundingCells[2] == 0:
                            MatrixNewGen[i - 1][j + 1] = 1
                            Matrix[i][j] = 0
                        else:
                            MatrixNewGen[i][j] = 1

            except:
                pass

    Matrix = MatrixNewGen

def randomize():
    global Matrix
    for object in Matrix:
        for i in range(len(object)):
            object[i] = random.randint(0, 1)

    for i in range(Size):
        Matrix[i][Size-1] = 2

def clear():
    global Matrix
    for object in Matrix:
        for i in range(len(object)):
            object[i] = 0

    for i in range(Size):
        Matrix[i][Size-1] = 2

def MouseSetting():
    global Matrix
    MouseCords = pygame.mouse.get_pos()
    MouseX = int(MouseCords[0] // (width/Size))
    MouseY = int(MouseCords[1] // (height/Size))
    Matrix[MouseX][MouseY] = 1



## SETUP VARIABLES ##

width, height = 650, 650
FPS = 30
pygame.display.set_caption("Falling Sand")
window = pygame.display.set_mode((width, height))

Size = 100
Matrix = makeGrid(Size, Size)

## SETUP VARIABLES ##
print("Press up key to unpause, down key to pause, left to randomize, and right to clear")
def main():
    clock = pygame.time.Clock()

    move = False

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        MouseSetting()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            move = False
        if keys[pygame.K_UP]:
            move = True
        if keys[pygame.K_LEFT]:
            randomize()
        if keys[pygame.K_RIGHT]:
            clear()

        if move:
            moveCells()
        updateWin()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()