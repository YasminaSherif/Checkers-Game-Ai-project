import pygame
from gui.checkersBoard import Board
from gui.measurements import *

class strategy:
    def __init__(self,window):
        self.selected = None
        self.board = Board()
        self.turn = black
        self.valid_moves = {}
        self.win = window

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self,row,col):
        if self.selected:
            result = self._move(row, col) # will move if the selected row and col is valid
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn: # لو ال بيس الي اختارتها متاحه و لون الشخص الي عليه الدور دا انا ف نفذ السيلكشن وانقل ال بيس
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False


    def winner(self):
        return self.board.winner()

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == black:
            self.turn = white
        else:
            self.turn = black

    def draw_valid_moves(self, moves):
        for move in moves:
            row , col = move
            pygame.draw.circle(self.win,green,(col * sq_size + sq_size//2, row * sq_size + sq_size//2),10)

    def get_board(self):
        return self.board

    def ai_move(self, board): # to set the board after the ai_move
        self.board = board
        self.change_turn()
