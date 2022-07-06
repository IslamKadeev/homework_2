import pygame
import sys
import numpy as np
from random import randint

pygame.init()

size_block = 50
margin = 15
width = height = size_block * 10 + margin * 11

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Обратные крестики нолики")

black = (0, 0, 0)
blue = (0, 0, 255)
mas = [[0] * 10 for i in range (10)]
query = 0



def check_draw(mas):
    if 0 in mas:
        return False
    else:
        return True

def check_lose(mas, sign):
    for row in range (10):
        for col in range(6):
            if mas[row][col] == mas[row][col + 1] == mas[row][col + 2] == mas[row][col + 3] == mas[row][col+4] == sign:
                return True
    
    for row in range(6):
        for col in range(10):
            if mas[row][col] == mas[row + 1][col] == mas[row + 2][col] == mas[row + 3][col] == mas[row + 4][col] == sign:
                return True

    for offset in range (-5, 6, 1):
        diagonal = np.diagonal(mas, offset, axis1 = 0, axis2 = 1)
        diagonal2 = np.diagonal(mas[ : : -1], offset, axis1 = 0, axis2 = 1)
        sign_counter = 0

        for element in diagonal:
            if element == sign:
                sign_counter += 1
                if sign_counter == 5:
                    return True
            else:
                sign_counter = 0
        
        for element in diagonal2:
            if element == sign:
                sign_counter += 1
                if sign_counter == 5:
                    return True
            else:
                sign_counter = 0
        

    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    row = randint(0, 9)
                    col = randint(0, 9)

                    while mas[row][col] != 0:
                        row = randint(0, 9)
                        col = randint(0, 9)
                    
                    mas[row][col] = 'o'

                query += 1

    for row in range(10):
        for col in range(10):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, blue, (x, y, size_block, size_block))

            if mas[row][col] == 'x':    
                pygame.draw.line(screen, black, (x + 5, y + 5),
                        (x + size_block - 5, y + size_block - 5), 3)
                pygame.draw.line(screen, black, (x + size_block - 5, y + 5),
                        (x + 5, y + size_block - 5), 3)
            elif mas[row][col] == 'o':
                pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2),
                                   size_block // 2, 3)
    

    pygame.font.init()
    f1 = pygame.font.Font(None, 60)

    if  not check_draw:
        text1 = f1.render('Ничья', True, (0, 180, 0))
        screen.fill(black)
        screen.blit(text1, (250, 250))
        mas = [[1] * 10 for i in range (10)]
    elif check_lose(mas,'x'):
        text1 = f1.render('Победа Х', True, (0, 180, 0))
        screen.fill(black)
        screen.blit(text1, (250, 250))
        mas = [[1] * 10 for i in range (10)]
    elif check_lose(mas,'o'):
        text1 = f1.render('Победа О', True, (0, 180, 0))
        screen.fill(black)
        screen.blit(text1, (250, 250))
        mas = [[1] * 10 for i in range (10)]

    pygame.display.update()

