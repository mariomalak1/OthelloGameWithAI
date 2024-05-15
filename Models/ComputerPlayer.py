import random
from copy import deepcopy

from .Player import Player
from .Disk import Disk


class ComputerPlayer(Player):
    _easyLevel = 1
    _mediumLevel = 3
    _hardLevel = 5

    def __init__(self, color, levelOfDifficulty=0):
        super().__init__("computer", color)
        self.difficulty = {1: self._easyLevel, 2: self._mediumLevel, 3: self._hardLevel}[levelOfDifficulty]

    def __str__(self):
        return f"Computer player with {self.color}"

    def getInputFromComputer(self, board, possibleMoves: list) -> int:
        if not possibleMoves:
            return None
        if self.difficulty == 1:  # If the difficulty is set to easy, choose randomly
            return random.choice(possibleMoves).position
        best_move, best_score = self.alpha_beta(board, self.difficulty, -float('inf'), float('inf'), True)

        # if algoritm get solution return it, else return any random value from list
        if best_move:
            return best_move.position
        return random.choice(possibleMoves).position

    def alpha_beta(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or board.noEmptyDisk():
            return None, self.evaluate_board(board)

        if maximizingPlayer:
            max_eval = float('-inf')
            best_move = None
            for move in board.getPossibleMovesForPlayer(self):
                simulated_board = self.cloneBoard(board)
                self.simulateMove(simulated_board, move.position, self.color)
                _, eval = self.alpha_beta(simulated_board, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        else:
            min_eval = float('inf')
            best_move = None
            for move in board.getPossibleMovesForPlayer(self):
                simulated_board = self.cloneBoard(board)
                self.simulateMove(simulated_board, move.position, self.color)
                _, eval = self.alpha_beta(simulated_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return best_move, min_eval

    def cloneBoard(self, board):

        return deepcopy(board)

    def simulateMove(self, board, position, color):
        # Assume position is already a valid move
        new_disk = Disk(color=color, position=position)
        board.putDiskInPosition(new_disk)  # Place the new disk on the board
        disks_to_flip = board.getFlibs(new_disk)  # Find all disks to flip as a result of this move
        board.flibDisks(disks_to_flip)  # Flip the disks

    def evaluate_board(self, board):

        black_score = board.score[0]
        white_score = board.score[1]

        # Strategic positions: corners
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        corner_value = 3
        black_corners = 0
        white_corners = 0

        for x, y in corners:
            if board.holeBoard[x][y].color == "black":
                black_corners += 1
            elif board.holeBoard[x][y].color == "white":
                white_corners += 1

        # legal movess
        black_mobility = len(board.getPossibleMovesForPlayer(Player(None, "black")))
        white_mobility = len(board.getPossibleMovesForPlayer(Player(None, "white")))
        mobility_value = 0.5  # Adjust weight as needed

        #  score components
        if self.color == "black":
            my_corner_control = black_corners * corner_value
            opponent_corner_control = white_corners * corner_value
            my_mobility = black_mobility * mobility_value
            opponent_mobility = white_mobility * mobility_value
        else:
            my_corner_control = white_corners * corner_value
            opponent_corner_control = black_corners * corner_value
            my_mobility = white_mobility * mobility_value
            opponent_mobility = black_mobility * mobility_value

        score = (black_score - white_score) + (my_corner_control - opponent_corner_control) + (
                my_mobility - opponent_mobility)
        return score
