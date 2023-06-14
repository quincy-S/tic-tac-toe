class Board:
    def __init__(self):
        self.spots = [["-","-","-"],["-","-","-"],["-","-","-"]]
        self.draw([[1,2,3],[4,5,6],[7,8,9]])

    def draw(self, boardSpots=None):
        if boardSpots is None:
            arr = self.spots
        else:
            arr = boardSpots
        for num in range(len(arr)):
            print(f"| {arr[num][0]} | {arr[num][1]} | {arr[num][2]} |")
            if num == 2:
                break
            print("+---+---+---+")
        
    def play(self, position, player):
        (x,y) = position.spotForNumber()
        self.spots[x][y] = player

    def validatePosition(self, position):
         while True: 
            (x,y) = position.spotForNumber()
            if self.spots[x][y] is not "-":
                print("You can't put your piece on a filled spot.")
                return False
            else:
                return True