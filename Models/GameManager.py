from . import Player, Board, Disk

class GameManager:
    _PlayWithComputer = 1
    _PlayWithSomeOne = 2

    def __init__(self):
        self.board = Board.Board()

        self.player1 = Player.Player(None, None)
        self.player2 = Player.Player(None, None)
        self.playWay = 0

    # will start the game from scratch, and ask the first user his name
    def start(self):
        print("Welcome Othello Game")

        # first player will be black
        name = input("What's your name : ")
        self.player1.name = name
        self.player1.color = "black"

        # create four disks as a begin of the game, and center them in the middle
        blackDisk1 = Disk.Disk("black", 29)
        blackDisk2 = Disk.Disk("black", 36)
        whiteDisk1 = Disk.Disk("white", 28)
        whiteDisk2 = Disk.Disk("white", 37)

        self.board.putDiskInPosition(whiteDisk1)
        self.board.putDiskInPosition(blackDisk1)
        self.board.putDiskInPosition(blackDisk2)
        self.board.putDiskInPosition(whiteDisk2)

        self.main()

    # has all logic for the game play
    def game(self):
        while True:
            while True:
                possibleMovesPlayer1 = self.board.getPossibleMovesForPlayer(self.player1)
                self.board.printBoard(possibleMovesPlayer1)
                playerMove = self.player1.getInput()
                disk = self.board.getDiskFromPostion(playerMove)
                if disk in possibleMovesPlayer1:
                    disk.putColor(self.player1.color)
                    break
                else:
                    print("Enter position for move that in avaliable only.")

            # check that the game is end
            if self.board.noEmptyDisk():
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
        if self.board.score[0] > self.board.score[1]:
            return self.player1
        elif self.board.score[0] < self.board.score[1]:
            return self.player2
        return None

    def checkDraw(self) -> bool:
        if self.board.score[0] == self.board.score[1]:
            return True
        return False

    # will check can the player play his turn or not
    def checkStatus(self, player):
        possiblePlays = self.board.getPossibleMovesForPlayer(player)
        if possiblePlays:
            return possiblePlays
        return None
