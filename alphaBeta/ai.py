from copy import deepcopy  # to copy the updates of board
import pygame
from math import inf
from gui.measurements import black,white

def alpha_beta(position, depth, alpha, beta, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxevaluation = -inf
        best_move = None
        for move in get_all_moves(position, white, game):
            evaluation = alpha_beta(move, depth-1, alpha, beta, False, game)[0]
            maxevaluation = max(maxevaluation,evaluation)
            alpha = max(alpha,evaluation)
            if beta <= alpha:
                break
            if maxevaluation == evaluation:
                best_move = move
        return  maxevaluation, best_move

    else:
        minevaluationl = inf
        best_move = None
        for move in get_all_moves(position, black, game):
            evaluation = alpha_beta(move, depth-1,alpha,beta, True, game)[0]
            minevaluationl = min(minevaluationl,evaluation)
            beta = min(beta,minevaluationl)
            if beta<= alpha:
                break
            if minevaluationl == evaluation:
                best_move = move
        return minevaluationl, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves
