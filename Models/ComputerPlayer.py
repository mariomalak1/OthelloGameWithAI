from .Player import Player


class ComputerPlayer(Player):

    def __init__(self, color, levelOfDiffcaltiy = 0):
        super().__init__("computer", color)
        self.diffcaltiy = levelOfDiffcaltiy

    def __str__(self):
        return f"Computer player with {super().color}"

    # will return valid input for a user from 1 to 64
    def getInputFromComputer(self, possibleMoves: list) -> int:
        while True:
            number = self.diffcaltiy
            try:
                disk = possibleMoves[number]
                return disk.position
                break
            except:
                number -= 1
