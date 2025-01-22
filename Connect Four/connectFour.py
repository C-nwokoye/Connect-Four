'''
Author: UJ Nwokoye
Lab:    08
File:   connectFour.py
This program is the connect four game, where for of the same token either horizontally or vertically wins the game.
'''

def main():
   # Creates a two dimensional board for the game, filled with spaces
   board = [[' ' for x in range(7)] for y in range(6)]

   # Sets up turn and game state
   turn = 1
   tokens = ['R', 'Y']
   gameOver = False
   
   # Game loop
   while not gameOver:
   
      # What turn is it?
      turn = (turn + 1) % len(tokens)
      
      # Show the board to the player
      display(board)
      
      # Prompt for which column
      column = int(input("Enter the column for turn " + tokens[turn] + ": "))
      
      # Obtain the row it ended up
      row = placeToken(board, column, tokens[turn])
      # Check for winning move

      gameOver = winningMove(board, column, row)
      
   # Display the board one last time if the game is over
   display(board)

   print("Game over!")
   print(tokens[turn], "won!")

def winningMove(board, column, row):
   if checkHorizontal(board, column, row) or checkVertical(board, column, row):
      return True
   else:
      return False

def checkHorizontal(board, column, row):
   # returns true if 4 of the same token are in the same row
   token = board[row][column]
   for i in range(4):
      count = 0
      if board[row][i] == token:
         for x in range(1,4):
            if board[row][i+x] == board[row][i]:
               count +=1
            else:
               break
         if count == 3:
            return True
   return False


def checkVertical(board, column, row):
   # returns true if 4 of the same token in the same column
   token = board[row][column]
   if row > len(board)-4:
      return False
   for i in range(4):
      if board[row+i][column] == token:
         pass
      else:
         return False
   return True

def placeToken(board, column, token):
   print(len(board))
   for i in range(1,len(board)):
      if board[len(board)-i][column] == ' ':
         board[len(board)-i][column] = token
         return(int(len(board)-i))


   
   
def display(board):
   # Join the tokens in the board to display it
   display = "\n".join(["| " + " | ".join(x) + " |" for x in board])
   
   print(display)
   print("-----" * len(board))
   
   # Show the column numbers
   print(" " + " ".join([" " + str(x) + " "  for x in range(len(board[0]))]))
   

if __name__ == '__main__':
   main()