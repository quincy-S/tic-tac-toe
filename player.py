class Player:
    def __init__(self):
        self.player = "X"

    def switchPlayer(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
       

    def getPlayer(self):
        return self.player