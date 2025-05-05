import time
import math
from copy import deepcopy

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(s == letter for s in row):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(s == letter for s in column):
            return True
        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all(s == letter for s in diag1) or all(s == letter for s in diag2):
                return True
        return False

    def is_draw(self):
        return ' ' not in self.board and self.current_winner is None


def minimax(board, player, maximizing, depth=0):
    opponent = 'O' if player == 'X' else 'X'
    if board.current_winner == player:
        return {'score': 1 * (10 - depth)}
    elif board.current_winner == opponent:
        return {'score': -1 * (10 - depth)}
    elif not board.empty_squares():
        return {'score': 0}

    best = {'score': -math.inf} if maximizing else {'score': math.inf}
    for move in board.available_moves():
        board_copy = deepcopy(board)
        board_copy.make_move(move, player if maximizing else opponent)
        sim_score = minimax(board_copy, player, not maximizing, depth+1)
        sim_score['move'] = move

        if maximizing:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    return best


def alphabeta(board, player, maximizing, alpha=-math.inf, beta=math.inf, depth=0):
    opponent = 'O' if player == 'X' else 'X'
    if board.current_winner == player:
        return {'score': 1 * (10 - depth)}
    elif board.current_winner == opponent:
        return {'score': -1 * (10 - depth)}
    elif not board.empty_squares():
        return {'score': 0}

    best = {'score': -math.inf} if maximizing else {'score': math.inf}
    for move in board.available_moves():
        board_copy = deepcopy(board)
        board_copy.make_move(move, player if maximizing else opponent)
        sim_score = alphabeta(board_copy, player, not maximizing, alpha, beta, depth+1)
        sim_score['move'] = move

        if maximizing:
            if sim_score['score'] > best['score']:
                best = sim_score
            alpha = max(alpha, best['score'])
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
            beta = min(beta, best['score'])

        if beta <= alpha:
            break
    return best


def compare_algorithms():
    game1 = TicTacToe()
    game2 = TicTacToe()

    print("Comparing Minimax vs Alpha-Beta Pruning on initial empty board:")
    
    start1 = time.time()
    move1 = minimax(game1, 'X', True)
    end1 = time.time()

    start2 = time.time()
    move2 = alphabeta(game2, 'X', True)
    end2 = time.time()

    print(f"Minimax chose move {move1['move']} in {end1 - start1:.6f} seconds.")
    print(f"Alpha-Beta Pruning chose move {move2['move']} in {end2 - start2:.6f} seconds.")
    print(f"Speedup: {(end1 - start1)/(end2 - start2):.2f}x")


if __name__ == "__main__":
    compare_algorithms()
