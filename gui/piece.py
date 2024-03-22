import pygame

from gui.measurements import *
class Piece:
    PADDING = 13
    OUTLINE = 2
    def __init__(self,row,col,color):
        self.row =row
        self.col =col
        self.color = color
        self.king =False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self): #calculate x and y position
        self.x=sq_size * self.col + sq_size // 2
        self.y=sq_size * self.row + sq_size // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = sq_size//2 - self.PADDING
        pygame.draw.circle(win,self.color,(self.x,self.y),radius)
        pygame.draw.circle(win,grey,(self.x,self.y),radius+self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y),radius)
        if self.king:
            win.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))

        pass
    def move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos();
    def __repr__(self):
        return str(self.color)