from .Player import Player

import random

class ComputerPlayer(Player):
    _easyLevel = 0
    _mediumLevel = 1
    _hardLevel = 2


    def __init__(self, color, levelOfDiffcaltiy = 0):
        super().__init__("computer", color)
        self.diffcaltiy = levelOfDiffcaltiy

    def __str__(self):
        return f"Computer player with {super().color}"

    # will return valid input for a user from 1 to 64
    def getInputFromComputer(self, possibleMoves: list) -> int:
        disk = random.choice(possibleMoves)
        return disk.position
