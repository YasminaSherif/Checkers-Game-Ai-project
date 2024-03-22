import pygame
from gui.measurements import width,height,sq_size,white,black  #import consent variable
from gui.gameStrategy import strategy
from alphaBeta.ai import alpha_beta
from math import inf

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkers') #name of game

def position_input(position):
    x,y=position
    row= y//sq_size
    col=x//sq_size
    return row, col

def main(): #the actuall game tha have the event loop
    start = True #open game
    clock = pygame.time.Clock() # keeps track of time
    game = strategy(WIN)
    while start:
        clock.tick(5) # update the clock
        if game.turn == white:
            value, new_board = alpha_beta(game.get_board(), 2, -inf, inf, white, game)
            game.ai_move(new_board)
        if game.winner() !=None:
            print(game.winner())
            start=False
        for event in pygame.event.get(): # collects all events that happend at a current time
            if event.type == pygame.QUIT: # this means terminate all events when we click exits
                start = False # close game
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col = position_input(pos)
                game.select(row,col)

        game.update()

    pygame.quit()

main()