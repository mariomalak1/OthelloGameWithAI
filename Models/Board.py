from colorama import Fore, Style

from .Disk import Disk

class Board:
    boardSize = 8

    def __init__(self):
        # in first the two players will have two disks
        # first score player1
        self.score = [2, 2]
        self.holeBoard = [[] for _ in range(8)]

        number = 0
        for row in self.holeBoard:
            for col in range(8):
                disk = Disk()
                number += 1
                disk.position = number
                row.append(disk)


    def printBoard(self, possibleMovesForPlayer = None):
        print("-" * 33)
        for row in self.holeBoard:
            print("|", end="")
            for disk in row:
                if disk.position < 10:
                    print(" ", end="")

                if possibleMovesForPlayer:
                    if disk.position in possibleMovesForPlayer:
                        print(f"{Fore.BLUE}{disk.position}", end="|")
                        continue
                print(disk.colorCode, end="")
                print(f"{disk.position} {Fore.RESET}", end="|")
            print(Style.RESET_ALL + "\n" + "-" * 33)

        black, white = self.getScoreNumber()

        print(f"Score Black : {black} | White : {white}")


    def putDiskInPosition(self, disk):
        col = (disk.position % Board.boardSize) - 1
        row = disk.position // Board.boardSize

        self.holeBoard[row][col] = disk

    def getScoreNumber(self):
        blackNumber = 0
        whiteNumber = 0

        for row in self.holeBoard:
            for disk in row:
                if disk.color == "black":
                    blackNumber += 1
                elif disk.color == "white":
                    whiteNumber += 1
        return blackNumber, whiteNumber

    def getPossibleMovesForPlayer(self, player):
        return [35, 21, 30, 44]

    def getFlibs(self):
        pass

