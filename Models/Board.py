class Board:
    boardSize = 8

    def __init__(self):
        number = 0
        self.holeBoard = [[] for _ in range(8)]
        for row in self.holeBoard:
            for col in range(8):
                number += 1
                row.append(number)


    def printBoard(self):
        print("-" * 33)
        for row in self.holeBoard:
            print("|", end="")
            for cell in row:
                if cell < 10:
                    print(f" {cell} ", end="|")
                else:
                    print(f" {cell}", end="|")
            print("\n" + "-" * 33)


    def getWhiteNumber(self):
        pass


    def getBlackNumber(self):
        pass


    def getPossibleMovesForPlayer(self, player):
        pass


    def getFlibs(self):
        pass

