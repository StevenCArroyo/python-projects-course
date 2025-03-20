
import os


def clear_screen():
	os.system("clear")

'''
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

'''

#print the board
def print_board(board):
	print(f"{board[0]} | {board[1]} | {board[2]}")
	print("--+---+--")
	print(f"{board[3]} | {board[4]} | {board[5]}")
	print("--+---+--")	
	print(f"{board[6]} | {board[7]} | {board[8]}")
	print()

#check winner
def check_winner(board, current_player):
	#define winning combos
	win_combinations = [
		#rows
		[0,1,2], [3,4,5], [6,7,8],
		#columns
		[0,3,6], [1,4,7], [2,5,8],
		#diagonals
		[0,4,8], [2,4,6],
	]
	#check if any combo is met
	for combination in win_combinations:
		if board[combination[0]] == board[combination[1]] == board[combination[2]] == current_player:
			return True
	return False

#check if draw
def check_draw(board):
	#loop through the board. If all items are an X or O then it's a draw
	return all(spot in ["X", "O"] for spot in board)


#main
def play_tic_tac_toe():
	#initialize board
	#['1', '2', '3', '4', '5', '6', '7', '8', '9']
	board = [str(i) for i in range(1,10)]
	#print(board)

	#define players
	current_player = "X"

	#Main game loop
	while True:
		clear_screen()
		print_board(board)
		
		#get player's move
		move = input(f"Player {current_player}, enter your move. 1-9: ")
		if not move.isdigit() or int(move) < 1 or int(move) > 9:
			print("Invalid input, enter a number between 1 and 9")
			continue

		#convert move to index 
		move = int(move) - 1

		#check if spot is taken
		if board[move] in ["X", "O"]:
			print("That spot is taken. Try again.")
			continue

		#update board
		board[move] = current_player

		#check if current_player has won
		if check_winner(board, current_player):
			clear_screen()
			#update board
			print_board(board)
			print(f"Player {current_player} wins!")
			break

		#check if game is draw
		if check_draw(board):
			clear_screen()
			print_board(board)
			print("It's a draw!")
			break


		#switch players
		current_player = "O" if current_player == "X" else "X"


play_tic_tac_toe()



