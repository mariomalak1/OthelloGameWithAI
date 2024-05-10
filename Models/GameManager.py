from . import Player, Board

class GameManager:
    _PlayWithComputer = 1
    _PlayWithSomeOne = 2

    def __init__(self):
        self.board = Board.Board()
        self.player1 = Player.Player(None, None)
        self.player2 = Player.Player(None, None)
        self.playWay = 0

        # in first the two players will have two disks
        # first score player1
        self.score = [2, 2]

    # will start the game from scratch, and ask the first user his name
    def start(self):
        print("Welcome Othello Game")

        # first player will be black
        name = input("What's your name : ")
        self.player1.name = name
        self.player1.color = "black"

        self.main()

    # has all logic for the game play
    def game(self):
        while True:
            self.board.printBoard()
            print(f"Score Black : {self.score[0]} | White : {self.score[1]}")

            # check for draw
            if self.checkDraw():
                print("No one is winner, it's draw.")
                self.endOfGame()

            # check if anyone win
            winner = self.checkWinner()

            if winner:
                if winner.name == "computer":
                    print("you lose.")
                self.endOfGame()


    # will get all needed data from user -> like name, color, need to play with computer or someone as an opponent
    def main(self):
        # ask him to play with computer or will play with someone
        while True:
            wayToPlay = input(
                f"hey {self.player1.name} if you want to play with computer press Y, else if you want to play with someone press X :")
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

    def endOfGame(self):
        print("game finish.")
        playAgain = input("if you want to play again press Y, else press X: ")
        if playAgain.lower() == "x":
            print("Bye.")
            exit(0)
        elif playAgain.lower() == "y":
            self.main()

    # will check that any player is winner
    def checkWinner(self) -> Player.Player:
        if self.score[0] > self.score[1]:
            return self.player1
        elif self.score[0] < self.score[1]:
            return self.player2
        return None

    def checkDraw(self) -> bool:
        if self.score[0] == self.score[1]:
            return True
        return False

    # will check can the player play his turn or not
    def checkStatus(self, player):
        possiblePlays = self.board.getPossibleMovesForPlayer(player)
        if possiblePlays:
            return possiblePlays
        return None

    def updateScore(self):
        black = self.board.getBlackNumber()
        white = self.board.getWhiteNumber()

        self.score[0] = black
        self.score[1] = white

