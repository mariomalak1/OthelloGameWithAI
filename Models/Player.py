from . import Board

class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # will return valid input for a user from 1 to 64
    def getInput(self) -> int:
        while True:
            try:
                num = int(input(f"{self.name}, Enter place for your play as number from 1 to 64 : "))

                if num < 0 or num > 64:
                    print("you can't play outside board size !, please enter valid number")
                else:
                    return num
                    break
            except:
                print("please enter valid number.")

    def __str__(self):
        return f"Player Name : {self.name} it's color : {self.color}"
