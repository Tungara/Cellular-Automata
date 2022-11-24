import pygame
import random
pygame.init()


def makeGrid(rows, columns):
    Matrix = [[0 for x in range(rows)] for y in range(columns)]

    for object in Matrix:
        for i in range(len(object)):
            object[i] = 0

    return Matrix


def updateWin():
    global Size, Matrix, window, height

    # Sets the pixels
    pixel_size = width / Size
    for i in range(Size):
        for j in range(Size):
            if Matrix[i][j] == 0:
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(pixel_size*i, pixel_size*j, pixel_size, pixel_size))
            elif Matrix[i][j] == 1:
                pygame.draw.rect(window, (0, 0, 0), pygame.Rect(pixel_size*i, pixel_size*j, pixel_size, pixel_size))

    # draws grid lines
    for line in range(Size):
        pass
        pygame.draw.line(window, (116, 116, 116), (0, line * width/Size), (width, line * width/Size))
        pygame.draw.line(window, (116, 116, 116), (line * height/Size, 0), (line * height/Size, height))

    pygame.display.update()


def moveCells():
    global Matrix
    MatrixNewGen = makeGrid(Size, Size)
    for i in range(Size):
        for j in range(Size):
            surroundingCount = 0
            try:
                surroundingCells = [Matrix[i-1][j-1], Matrix[i-1][j+0], Matrix[i-1][j+1],
                                    Matrix[i+0][j-1],                   Matrix[i+0][j+1],
                                    Matrix[i+1][j-1], Matrix[i+1][j+0], Matrix[i+1][j+1]]

            except:
                if i==(Size-1):
                    surroundingCells = [Matrix[i-1][j]]
                if j == (Size-1):
                    surroundingCells = [Matrix[i + 0][j - 1]]


            for cell in surroundingCells:
                surroundingCount += cell



            if Matrix[i][j] == 0:
                if surroundingCount == 1:
                    MatrixNewGen[i][j] = 1
            elif Matrix[i][j] == 1:
                MatrixNewGen[i][j] = Matrix[i][j]

    Matrix = MatrixNewGen

def randomize():
    global Matrix
    for object in Matrix:
        for i in range(len(object)):
            chance = random.randint(0, 50)
            if chance == 1:
                object[i] = 1

def clear():
    global Matrix
    for object in Matrix:
        for i in range(len(object)):
            object[i] = 0

def MouseSetting():
    global Matrix
    MouseCords = pygame.mouse.get_pos()
    MouseX = int(MouseCords[0] // (width/Size))
    MouseY = int(MouseCords[1] // (height/Size))
    if Matrix[MouseX][MouseY] == 1:
        Matrix[MouseX][MouseY] = 0
    elif Matrix[MouseX][MouseY] == 0:
        Matrix[MouseX][MouseY] = 1



## SETUP VARIABLES ##

width, height = 650, 650
FPS = 30
pygame.display.set_caption("Pattern 0/1/1/M")
window = pygame.display.set_mode((width, height))

Size = 150
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse Button
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