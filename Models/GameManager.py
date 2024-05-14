from . import Player, Board, Disk, ComputerPlayer

class GameManager:
    _PlayWithComputer = 1
    _PlayWithSomeOne = 2

    def __init__(self):
        self.board = Board.Board()

        self.player1 = Player.Player(None, "black")
        self.player2 = Player.Player(None, "white")
        self.playWay = 0

    # will start the game from scratch, and ask the first user his name
    def start(self):
        print("Welcome Othello Game")

        # first player will be black
        name = input("What's your name : ")

        print(f"Hey {name}, ", end="")
        while True:
            blackOrWhite = input(f"you want to play with black or white, for black enter b, for white enter w : ")
            if blackOrWhite.lower() == "b":
                self.player1.name = name
                break
            elif blackOrWhite.lower() == "w":
                self.player2.name = name
                break
            else:
                print("please enter valid response.")

        # create four disks as a begin of the game, and center them in the middle
        blackDisk1 = Disk.Disk("black", 29)
        blackDisk2 = Disk.Disk("black", 36)
        whiteDisk1 = Disk.Disk("white", 28)
        whiteDisk2 = Disk.Disk("white", 37)

        self.board.putDiskInPosition(whiteDisk1)
        self.board.putDiskInPosition(blackDisk1)
        self.board.putDiskInPosition(blackDisk2)
        self.board.putDiskInPosition(whiteDisk2)

        self.gameHome()

    # and get all needed data from user -> like name, color, need to play with computer or someone as an opponent
    def gameHome(self):
        # ask him to play with computer or will play with someone
        while True:
            wayToPlay = input(
                "if you want to play with computer press Y, else if you want to play with someone press X :")
            if wayToPlay.lower() == "y":
                diff = self.chooseDiffcultyPlayingWithComputer()
                self.playWay = GameManager._PlayWithComputer

                if self.player1.name:
                    self.player2 = ComputerPlayer.ComputerPlayer("white", diff)
                else:
                    self.player1 = ComputerPlayer.ComputerPlayer("black", diff)
                break
            elif wayToPlay.lower() == "x":
                self.playWay = GameManager._PlayWithSomeOne
                name = input("What's his name : ")
                if self.player1.name:
                    self.player2.name = name
                    self.player2.color = "white"
                else:
                    self.player1.name = name
                    self.player1.color = "black"
                break
            else:
                print("please enter valid input.")

        self.game()

    # has all logic for the game play
    def game(self):
        skipList = []

        if self.playWay == self._PlayWithComputer:
            while True:
                if self.player1.name == "computer":
                    self.computerPlay(self.player1, skipList)
                    self.HumanPlay(self.player2, skipList)
                else:
                    self.HumanPlay(self.player1, skipList)
                    self.computerPlay(self.player2, skipList)

                # check that the game is end
                # check if no one can play for now, then show the results
                if self.board.noEmptyDisk() or len(skipList) == 2:
                    self.board.printBoard()
                    # check for draw
                    if self.checkDraw():
                        print("No winner, it's draw.")
                        break

                    # check if anyone win
                    winner = self.checkWinner()

                    if winner:
                        if winner.name == "computer":
                            print("you lose.")
                        else:
                            print("congratulations, you are win")
                        break
                else:
                    skipList.clear()
        else:
            while True:
                self.HumanPlay(self.player1, skipList)
                self.HumanPlay(self.player2, skipList)

                # check that the game is end
                # check if no one can play for now, then show the results
                if self.board.noEmptyDisk() or len(skipList) == 2:
                    self.board.printBoard()
                    # check for draw
                    if self.checkDraw():
                        print("No one is winner, it's draw.")
                        break

                    # check if anyone win
                    winner = self.checkWinner()

                    if winner:
                        print(f"the winner is {winner.name} with color {winner.color}")
                        break
                else:
                    skipList.clear()

        self.endOfGame()

    def computerPlay(self, computerPlayer: ComputerPlayer, skipList: list):
        possibleMovesPlayer = self.board.getPossibleMovesForPlayer(computerPlayer)
        if possibleMovesPlayer:
            computerPlayerMove = computerPlayer.getInputFromComputer(self.board, possibleMovesPlayer)
            disk = self.board.getDiskFromPosition(computerPlayerMove)

            if disk in possibleMovesPlayer:
                disk.putColor(computerPlayer.color)
                disk.color = computerPlayer.color
                disksNeedToFlib = self.board.getFlibs(disk)
                if disksNeedToFlib:
                    self.board.flibDisks(disksNeedToFlib)
        else:
            print("Computer turn skipped.")
            skipList.append(1)

    def HumanPlay(self, player, skipList):
        while True:
            possibleMovesPlayer = self.board.getPossibleMovesForPlayer(player)
            if possibleMovesPlayer:
                self.board.printBoard(possibleMovesPlayer)
                playerMove = player.getInput()
                disk = self.board.getDiskFromPosition(playerMove)

                if disk in possibleMovesPlayer:
                    disk.putColor(player.color)
                    disk.color = player.color
                    disksNeedToFlib = self.board.getFlibs(disk)
                    if disksNeedToFlib:
                        self.board.flibDisks(disksNeedToFlib)
                        break
                else:
                    print("Enter position for move that is available only.")
            else:
                print("Your turn skipped.")
                skipList.append(1)
                break
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

    def chooseDiffcultyPlayingWithComputer(self):
        while True:
            try:
                diff = int(input("choose diffculty from easy, medium, and hard as 1, 2, 3 respectivly: "))
                if diff in [1, 2, 3]:
                    return diff
                    break
                else:
                    print("please enter valid number from 1, 2, 3.")
            except:
                print("please enter valid response.")
