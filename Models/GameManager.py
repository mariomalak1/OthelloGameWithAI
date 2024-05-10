from . import Player, Board

class GameManager:
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None

    # has all logic for the game play
    def game(self):
        pass

    # will get all needed data from user -> like name, color , need to play with computer or someone as an opponent
    def start(self):
        pass

    # will check that any player is winner or it's draw or nothing
    def checkWinner(self):
        pass

    # will check can the player play his turn or not
    def checkStatus(self):
        pass

    def getScore(self):
        pass
