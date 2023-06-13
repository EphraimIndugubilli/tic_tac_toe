import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possible_numbers = [1,2,3,4,5,6,7,8,9]
game_board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def print_game_board():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", game_board[x][y], end=" |")
  print("\n+---+---+---+")

def modify_array(num, turn):
  num -= 1
  if (num == 0):
    game_board[0][0] = turn
  elif(num == 1):
    game_board[0][1] = turn
  elif(num == 2):
    game_board[0][2] = turn 
  elif(num == 3):
    game_board[1][0] = turn
  elif(num == 4):
    game_board[1][1] = turn
  elif(num == 5):
    game_board[1][2] = turn
  elif(num == 6):
    game_board[2][0] = turn
  elif(num == 7):
    game_board[2][1] = turn    
  elif(num == 8):
    game_board[2][2] = turn 


def check_for_winner(game_board):
  if(game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O'):
    print("O has won!")
    return "O"

  if(game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(game_board[0][2] == 'X' and game_board[1][2] == 'X' and game_board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[0][2] == 'O' and game_board[1][2] == 'O' and game_board[2][2] == 'O'):
    print("O has won!")
    return "O"

  elif(game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"


leave_loop = False
turn = 'x'
turn_counter = 0

while(leave_loop == False):
  if(turn_counter % 2 == 1):
    print_game_board()
    number_picked = int(input("\nchoose a number[1-9]: "))
    if(number_picked >= 1 or number_picked <= 9):
      modify_array(number_picked,'x')
      possible_numbers.remove(number_picked)
    else:
      print("Invaild input. Please try again")
    turn_counter += 1
  else:
    while(True):
      cpu_choice = random.choice(possible_numbers)
      print("\nCpu choice: ",cpu_choice)
      if(cpu_choice in possible_numbers):
        modify_array(cpu_choice,'O')
        possible_numbers.remove(cpu_choice)
        turn_counter += 1
        break

  winner = check_for_winner(game_board)
  if(winner != "N"):
    print("\nGame over! Thank you for playing 😁")
    break

