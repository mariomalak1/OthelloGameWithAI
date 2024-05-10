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


    def getRowColOfDisk(self, position):
        col = (position % Board.boardSize) - 1
        row = position // Board.boardSize
        return row, col


    def putDiskInPosition(self, disk):
        row, col = self.getRowColOfDisk(disk.position)
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

    # to get all disks around a disk that empty
    def getAllEmptyDisksAroundDisk(self, disk: Disk) -> list:
        row, col = self.getRowColOfDisk(disk.position)
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

    # get all disks needed to flibs
    def getFlibs(self, playedDisk: Disk):
        getFlibed = []

        row, col = self.getRowColOfDisk(playedDisk.position)
        rightBranch, leftBranch = self.getAllDisksInDiagonal(row, col)
        allDisksInRow = self.getAllDisksInRow(row)
        allDisksInCol = self.getAllDisksInCol(col)

        branches = [allDisksInCol, rightBranch, leftBranch, allDisksInRow]

        for branch in branches:
            position = 0
            mayFlibed = []

            while True:
                disk = branch[position]
                if disk == playedDisk:

                    # try to get left way
                    copyPoistion = position
                    while True:
                        if copyPoistion > 0:
                            copyPoistion -= 1
                            disk2 = branch[copyPoistion]
                            if not disk2.color:
                                mayFlibed.clear()
                                break
                            else:
                                print("disk2.color : ", disk2.color, " playedDisk.color : ", playedDisk.color)
                                if disk2.color != playedDisk.color:
                                    mayFlibed.append(disk2)
                                else:
                                    getFlibed += mayFlibed
                                    break
                        else:
                            break

                    # try to get right way
                    copyPoistion = position
                    while True:
                        if copyPoistion < 7:
                            copyPoistion += 1
                            disk2 = branch[copyPoistion]
                            if not disk2.color:
                                mayFlibed.clear()
                                break
                            else:
                                print("disk2.color : ", disk2.color, " playedDisk.color : ", playedDisk.color)
                                if disk2.color != playedDisk.color:
                                    mayFlibed.append(disk2)
                                else:
                                    getFlibed += mayFlibed
                                    break
                        else:
                            break
                    break
                else:
                    position += 1


        # to remove dublicates
        getFlibed = list(set(getFlibed))

        print(getFlibed)

        return getFlibed

    def getAllDisksInRow(self, row: int):
        if row > 7 or row < 0:
            return []
        return self.holeBoard[row]

    def getAllDisksInCol(self, col: int):
        disksInCol = []
        if col > 7 or col < 0:
            return disksInCol

        for row in self.holeBoard:
            disksInCol.append(row[col])
        return disksInCol

    def getAllDisksInDiagonal(self, row: int, col: int):
        rightDiagonal = []
        leftDiagonal = []

        # append the played disk in the branch
        disk = self.holeBoard[row][col]
        rightDiagonal.append(disk)
        leftDiagonal.append(disk)

        copyRow = row
        copyCol = col

        # get right diagonal

        # get the upper part
        while True:
            copyRow -= 1
            copyCol += 1
            if (copyRow <= 7 and copyRow >= 0 and copyCol <= 7 and copyCol >= 0):
                print(copyRow, copyCol)
                disk = self.holeBoard[copyRow][copyCol]
                rightDiagonal.append(disk)
            else:
                break

        # get the lower part
        copyRow = row
        copyCol = col

        while True:
            copyRow += 1
            copyCol -= 1
            if (copyRow <= 7 and copyRow >= 0 and copyCol <= 7 and copyCol >= 0):
                disk = self.holeBoard[copyRow][copyCol]
                rightDiagonal.append(disk)
            else:
                break

        # sort the right branch
        rightDiagonal = sorted(rightDiagonal, key=lambda x: x.position)

        # get left diagonal
        # get the upper part
        copyRow = row
        copyCol = col

        while True:
            copyRow -= 1
            copyCol -= 1
            if (copyRow <= 7 and copyRow >= 0 and copyCol <= 7 and copyCol >= 0):
                disk = self.holeBoard[copyRow][copyCol]
                leftDiagonal.append(disk)
            else:
                break

        # get the lower part
        copyRow = row
        copyCol = col

        while True:
            copyRow += 1
            copyCol += 1
            if (copyRow <= 7 and copyRow >= 0 and copyCol <= 7 and copyCol >= 0):
                disk = self.holeBoard[copyRow][copyCol]
                leftDiagonal.append(disk)
            else:
                break

        # sort left branch
        leftDiagonal = sorted(leftDiagonal, key=lambda x: x.position)

        return rightDiagonal, leftDiagonal


    def flibDisks(self, needToFlib: list):
        for disk in needToFlib:
            disk.flipDisk()


    def getDiskFromPostion(self, position):
        row, col = self.getRowColOfDisk(position)
        return self.holeBoard[row][col]

    # check that no empty disk found
    def noEmptyDisk(self) -> bool:
        for row in self.holeBoard:
            for cell in row:
                if not cell.color:
                    return False
        return True
