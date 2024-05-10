from . import Player, Board

class GameManager:
    _PlayWithComputer = 1
    _PlayWithSomeOne = 2
    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.playWay = 0

    # has all logic for the game play
    def game(self):
        pass


    # will get all needed data from user -> like name, color, need to play with computer or someone as an opponent
    def start(self):
        print("Welcome Othello Game")

        # first player will be black
        name = input("What's your name : ")
        self.player1.name = name
        self.player1.color = "black"

        # ask him to play with computer or will play with someone
        while True:
            wayToPlay = input(f"hey {self.player1.name} if you want to play with computer press Y, else if you want to play with someone press X :")
            if wayToPlay.lower() == "y":
                self.playWay = GameManager._PlayWithComputer
                self.player2.name = "computer"
                self.player2.color = "white"
                break
            elif wayToPlay.lower() == "x":
                self.playWay = GameManager._PlayWithSomeOne
                name = input("What's his name : ")
                self.player2.name = name
                self.player2.color = "white"
                break
            else:
                print("please enter valid input.")

        # start the game pay
        self.game()


    # will check that any player is winner or it's draw or nothing
    def checkWinner(self):
        pass

    # will check can the player play his turn or not
    def checkStatus(self):
        pass

    def getScore(self):
        pass

