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
        return best_move.position if best_move else None

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

   
    def evaluate_board(self, board):
        #simple ocunter of disks  
        return board.score[0] if self.color == "black" else board.score[1]


    def cloneBoard(self):
        # Create a deep copy of the board
        return deepcopy(self)

    def simulateMove(self, board, position, color):
        # Assume position is already a valid move
        new_disk = Disk(color=color, position=position)
        board.putDiskInPosition(new_disk)  # Place the new disk on the board
        disks_to_flip = board.getFlibs(new_disk)  # Find all disks to flip as a result of this move
        board.flibDisks(disks_to_flip)  # Flip the disks

