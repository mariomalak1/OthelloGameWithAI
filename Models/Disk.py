from colorama import Fore

class Disk:
    def __init__(self, color = None, position = None, colorCode = None):
        self.color = color
        self.position = position

        if color == "black":
            self.colorCode = Fore.RED
        elif color == "white":
            self.colorCode = Fore.GREEN
        else:
            if colorCode:
                self.colorCode = colorCode
            else:
                self.colorCode = Fore.MAGENTA


    def flipDisk(self):
        if self.color == "black":
            self.color = "white"
            self.colorCode = Fore.GREEN
        else:
            self.color = "black"
            self.colorCode = Fore.RED

    def __str__(self):
        str_ = str(self.position)
        if self.color:
            str_ += " Color : " + self.color
        return str(str_)
