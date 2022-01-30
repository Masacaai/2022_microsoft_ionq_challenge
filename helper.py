import pygame
import sys


def words(text, size, color, x_location, y_location, window):
    font = "monospace"
    type = pygame.font.SysFont(font, size)
    words = type.render(text, True, color)
    wordsRect = words.get_rect()
    wordsRect.center = (x_location, y_location)
    window.blit(words, wordsRect)


def drawbutton(color, position, text, text_color, size, window):
    pygame.draw.rect(window, color, position)
    words(text, size, text_color, position[0] + (position[2] // 2), position[1] + (position[3] // 2), window)


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows
    x = 40
    y = 40
    for l in range(rows - 9):
        y = y + sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (120, y), (1160, y))

    for l in range(rows - 2):
        x = x + sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (x, 120), (x, 600))

def score(size,x,y,list,window, color = (255,255,255)):
    score_keeper = "Score: "+str(len(list))
    words(score_keeper,size,color,x,y,window)

def timer(size,x,y,start_time, window):
    global counting_string
    counting_time = pygame.time.get_ticks() - start_time

    # change milliseconds into minutes, seconds, milliseconds
    counting_minutes = str(counting_time // 60000).zfill(2)
    counting_seconds = str((counting_time % 60000) // 1000).zfill(2)

    counting_string = "%s:%s" % (counting_minutes, counting_seconds)
    words(counting_string,size,(255,255,255),x,y, window)

def checkforexit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()