class TicTacToe(object):
	board = ["", "", "", "", "", "", "", "", ""]
	isWon = False

	def __init__(self, p1=None, p2=""):
		self.p1 = p1
		self.p2 = p2

		self.currentPlayer = p1

	def game(self):
		while(self.isWon == False):
			print("{0}'s Turn".format(self.currentPlayer.name))

			idx = self.currentPlayer.place_mark()

			while self.board[idx - 1] != "":
				print("That spot is already taken")
				idx = self.currentPlayer.place_mark()

			self.board[idx - 1] = self.currentPlayer.mark
			
			self.isWon = self.checkWin(self.board)

			if(self.isWon):
				print("{0} Wins".format(self.currentPlayer.name))
				return
			else:
				if("" not in self.board):
					print("THE GAME IS DRAW!")
					return

				if self.currentPlayer == self.p1:
					self.currentPlayer = self.p2
				else:
					self.currentPlayer = self.p1

	def checkWin(self, board):
		winConditions = [
			[0, 1, 2],
			[3, 4, 5],
			[6, 7, 8],
			[0, 3, 6],
			[1, 4, 7],
			[2, 5, 8],
			[0, 4, 8],
			[2, 4, 6]
		]

		for win in winConditions:
			if self.board[win[0]] != "" and self.board[win[1]] != "" and self.board[win[1]] != "":
				if self.board[win[0]] == self.board[win[1]] and self.board[win[1]] == self.board[win[2]]:
					return True

		return False

def game():
	# 1. set board
	board = ["", "", "", "", "", "", "", "", ""]
	# 2. ready players
	p1 = Player(name="A", mark="X")
	p2 = Player(name="B", mark="O")
	# 3. declare first players
	currentPlayer = p1
	isWon = False

	while(isWon == False):
		print("{0}'s Turn".format(currentPlayer.name))

		idx = currentPlayer.place_mark()

		while board[idx - 1] != "":
			print("That spot is already taken")
			idx = currentPlayer.place_mark()

		board[idx - 1] = currentPlayer.mark
		
		isWon = checkWin(board)

		if(isWon):
			print("{0} Wins".format(currentPlayer.name))
			return
		else:
			if("" not in board):
				print("THE GAME IS DRAW!")
				return

			if currentPlayer == p1:
				currentPlayer = p2
			else:
				currentPlayer = p1


def checkWin(board):
	winConditions = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6]
	]

	for win in winConditions:
		if board[win[0]] != "" and board[win[1]] != "" and board[win[1]] != "":
			if board[win[0]] == board[win[1]] and board[win[1]] == board[win[2]]:
				return True

	return False

class Player(object):
	def __init__(self, name="", mark=""):
		self.name = name
		self.mark = mark

	def place_mark(self):
		while True:
			try:
				mark = int(input("Mark the board from 1 to 9:\n"))
				return mark
			except ValueError:
				print("That is not a valid input! Try again")



# game()

p1 = Player(name="A", mark="X")
p2 = Player(name="B", mark="O")
game = TicTacToe(p1, p2)

game.game()