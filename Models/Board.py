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
                    if disk in possibleMovesForPlayer:
                        print(f"{Fore.BLUE}{disk.position}", end="|")
                        continue
                print(disk.colorCode, end="")
                print(f"{disk.position} {Fore.RESET}", end="|")
            print(Style.RESET_ALL + "\n" + "-" * 33)

        black, white = self.getScoreNumber()

        print(f"Score Black : {black} | White : {white}")


    def getRowColOfDisk(self, disk):
        col = (disk.position % Board.boardSize) - 1
        row = disk.position // Board.boardSize
        return row, col


    def putDiskInPosition(self, disk):
        row, col = self.getRowColOfDisk(disk)
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
        allPossibleMoves = []
        for row in self.holeBoard:
            for cell in row:
                if cell.color:
                    if cell.color != player.color:
                        allEmptyDisksAround = self.getAllEmptyDisksAroundDisk(cell)
                        allPossibleMoves = list(set(allPossibleMoves + allEmptyDisksAround))

        return allPossibleMoves


    def getAllEmptyDisksAroundDisk(self, disk: Disk) -> list:
        row, col = self.getRowColOfDisk(disk)
        emptyDisks = []

        # get the left disk if found and not empty
        if not col - 1 < 0:
            disk1 = self.holeBoard[row][col - 1]
            if not disk1.color:
                emptyDisks.append(disk1)

        # get the right disk if found and not empty
        if not col + 1 > 7:
            disk2 = self.holeBoard[row][col + 1]
            if not disk2.color:
                emptyDisks.append(disk2)

        # get the above disk if found and not empty
        if not row - 1 < 0:
            disk3 = self.holeBoard[row - 1][col]
            if not disk3.color:
                emptyDisks.append(disk3)

        # get the down disk if found and not empty
        if not row + 1 > 7:
            disk4 = self.holeBoard[row + 1][col]
            if not disk4.color:
                emptyDisks.append(disk4)

        return emptyDisks


    def getFlibs(self):
        pass

