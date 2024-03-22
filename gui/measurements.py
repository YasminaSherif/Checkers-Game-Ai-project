import pygame
width = 500
height = 500
ROWS = 8
COLS = 8
sq_size = width//COLS #حجم المربع بتاع البورد
#RGB
beige= (250,151,70)
grey= (51,51,51)
black=(0,0,0)
white=(255,255,255)
green=(10,209,24)
img = pygame.transform.scale(pygame.image.load('unnamed.png'),(30,25))