import pygame
from gui.measurements import *
from .piece import Piece
class Board:
   def __init__(self):
    self.board =[]
    self.white_left = self.black_left = 12
    self.white_kings = self.black_kings = 0
    self.create_board()

   def draw_cubes(self, win):
    win.fill(grey)
    for row in range(ROWS):
        for col in range (row%2,COLS,2):
            pygame.draw.rect(win,beige,(row*sq_size, col*sq_size,sq_size,sq_size))
    pass

   def move(self, piece, row, col):
       self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
       piece.move(row, col)

       if row == ROWS - 1 or row == 0:
           piece.make_king()
           if piece.color == white:
               self.white_kings += 1
           else:
               self.black_kings += 1

   def get_piece(self,row,col):
       return self.board[row][col]

   def get_all_pieces(self, color):  # to return the numbers of pieces of a certain color in the board
       pieces = []
       for row in self.board:
           for piece in row:
               if piece != 0 and piece.color == color:
                   pieces.append(piece)
       return pieces

   """def evaluate(self):  # AI function # return the score the number of pieces we have and kings
       return self.white_left - self.black_left + (self.white_king * 0.5 - self.black_kings * 0.5) """

   def evaluate(self):
       white_rating=0
       black_rating=0
       for row in self.board:
           for piece in row:
               if piece != 0 and piece.color == white:
                   if piece.king:
                       white_rating+=5
                   else:
                       white_rating+=1
               elif piece != 0 and piece.color == black:
                   if piece.king:
                       black_rating+=5
                   else:
                       black_rating+=1
       return white_rating - black_rating

   def remove(self, pieces):
       for piece in pieces:
           self.board[piece.row][piece.col] = 0
           if piece != 0:
               if piece.color == black:
                   self.black_left -= 1
               else:
                   self.white_left -= 1

   def winner(self):
       if self.white_left <= 0:
           return black
       elif self.black_left <= 0:
           return white

       return None

   def create_board(self):
       for row in range(ROWS):
           self.board.append([])
           for col in range(COLS):
               if col % 2 == ((row + 1) % 2):
                   if row < 3:
                       self.board[row].append(Piece(row, col, white))
                   elif row > 4:
                       self.board[row].append(Piece(row, col, black))
                   else:
                       self.board[row].append(0)
               else:
                   self.board[row].append(0)
       pass

   def draw(self,win):
       self.draw_cubes(win)
       for row in range(ROWS):
           for col in range(COLS):
               piece = self.board[row][col]
               if piece != 0:
                   piece.draw(win)
       pass

   def get_valid_moves(self,piece):
       moves = {} #key is the move
       left = piece.col - 1 #بحرك البيس شمال يبقي بنقص 1 من العمود الي هي فيه
       right= piece.col + 1
       row =  piece.row

       if piece.color == black or piece.king:
           moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
           moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
       if piece.color == white or piece.king:
           moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
           moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))

       return moves

   def _traverse_left(self, start, stop, step, color, left, skipped=[]):
       moves = {}
       last = []
       for r in range(start, stop, step):
           if left < 0:
               break

           current = self.board[r][left]  # we found empty square
           if current == 0:
               if skipped and not last:
                   break
               elif skipped:  # douple jump?
                   moves[(r, left)] = last + skipped
               else:
                   moves[(r, left)] = last

               if last:
                   if step == -1:
                       row = max(r - 3, 0)
                   else:
                       row = min(r + 3, ROWS)
                   moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                   moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
               break
           elif current.color == color:
               break
           else:
               last = [current]  # هنحفظه و نتشيك الي بعده لو قاضي

           left -= 1

       return moves

   def _traverse_right(self, start, stop, step, color, right, skipped=[]):
       moves = {}
       last = []
       for r in range(start, stop, step):
           if right >= COLS:
               break

           current = self.board[r][right]
           if current == 0:
               if skipped and not last:
                   break
               elif skipped:
                   moves[(r, right)] = last + skipped
               else:
                   moves[(r, right)] = last

               if last:
                   if step == -1:
                       row = max(r - 3, 0)
                   else:
                       row = min(r + 3, ROWS)
                   moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                   moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
               break
           elif current.color == color:
               break
           else:
               last = [current]

           right += 1

       return moves
