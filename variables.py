import pygame
pygame.init()
# Initializations:
width = 1280
height = 720
rows = 16
dis = width // rows
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
rectangle_draging = True
offset_x = 0
offset_y = 0
gatenum = 0
type = pygame.font.SysFont("monospace", 20)
