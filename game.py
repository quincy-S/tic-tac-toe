from board import Board
from position import Position
from player import Player

class Game:

    def __init__(self):
        self.active = True

    def start(self):
        print("-----------------------------------------")
        print("Welcome to Tic-Tac-Toe by quincy-S")
        print("-----------------------------------------")
        print(" ")
        board = Board()
        player = Player()
        print(" ")
        print("-----------------------------------------")
        print("Each number corresponds to a position on the board.")
        print("Input a number to place your piece in the corresponding area.")
        print("-----------------------------------------")
        print(" ")

        while self.active:
            currentPlayer = player.getPlayer()
            print(f"Please make your move player {currentPlayer}")
            playerMove = self.getValidInput(currentPlayer)
            if board.validatePosition(Position(playerMove)) is True:
                board.play(Position(playerMove), currentPlayer)
                board.draw()
                if self.checkWin(board, currentPlayer):
                    print(f"Player {currentPlayer} wins! Play again?")
                    self.playAgain()      
                if self.isDraw(board):
                    print(f"This ended in a draw. Play again?")
                    self.playAgain()
                player.switchPlayer()
            else:
                continue
   
    def playAgain(self):
        playerChoice = input("Press Y to play again, any other button to quit: ")
        if playerChoice == "Y" or playerChoice == "y":
            self.start()
        else:
            self.end()


    def getValidInput(self,currentPlayer):
        while True:
            number = input()
            if number.isdigit() and 1 <= int(number) <=9:
                return int(number)
            else:
                print(f"Please enter a valid number between 1 and 9 player {currentPlayer}")

    def end(self):
        self.active = False
        return

    def checkWin(self,board, playerSymbol):
        print(playerSymbol)
        for row in range(len(board.spots)):
            if self.isAMatch([board.spots[row][0], board.spots[row][1], board.spots[row][2]], playerSymbol):
                return True

        for column in range(len(board.spots)):
            if self.isAMatch([board.spots[0][column], board.spots[1][column], board.spots[2][column]], playerSymbol):
                return True
        
        if self.isAMatch([board.spots[0][0], board.spots[1][1], board.spots[2][2]], playerSymbol):
            return True
        if self.isAMatch([board.spots[2][0], board.spots[1][1], board.spots[0][2]], playerSymbol):
            return True
        
        return False


    def isAMatch(self,items, player):
        numberMatched = 0
        for item in items:
            if item is player:
                numberMatched +=1
        if numberMatched == 3:
            return True
        return False    
            
            

    def isDraw(self,board):
        for row in range(len(board.spots)):
            for column in range(len(board.spots)):
                if board.spots[row][column] is "-":
                    return False
        return True
