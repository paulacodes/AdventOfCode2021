def get_numbers_and_boards():
	boards = []
	with open('inputs/day4.txt') as f:
		numbers = f.readline().rstrip().split(",")
		board = []
		position = 0
		for line in f:
			if "," in line:
				numbers = line.rstrip().split(",")
			elif line.rstrip() == "":
				if board != []:
					boards.append(board)
				board = []
				position = 0
			else:
				board.append([])
				board[position] = line.rstrip().split()
				position += 1 
	f.close()
	return boards, numbers

def mark_winners_in_board(board, number):
	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col] == number:
				board[row][col] = "x"
	return board

def check_if_board_is_winner(board):
	is_winner = False 
	for row in range(len(board)):
		row_check = 0
		for col in range(len(board)):
			if board[row][col] == "x":
				row_check += 1
		if row_check == 5:
			return True
	for col in range(len(board)):
		col_check = 0
		for row in range(len(board)):
			if board[row][col] == "x":
				col_check += 1
		if col_check == 5:
			return True
	for pos in range(len(board)):
		diag1_check = 0
		diag2_check = 0
		if board[pos][pos] == "x":
			diag1_check += 1
		if board[pos][pos-len(board)+1] == "x":
			diag2_check += 1
		if diag1_check == 5 or diag2_check == 5:
			return True
	return False

def part1():
	boards, numbers = get_numbers_and_boards()
	for number in numbers:
		board_pos = 0
		for board_pos in range(len(boards)):
			marked_board = mark_winners_in_board(boards[board_pos], number)
			boards[board_pos] = marked_board
			if check_if_board_is_winner(marked_board):
				sum_unmarked = 0
				for row in range(len(marked_board)):
					for col in range(len(marked_board)):
						if marked_board[row][col] != "x":
							sum_unmarked += int(marked_board[row][col])
				print(sum_unmarked * int(number))
				return True

def part2():
	boards, numbers = get_numbers_and_boards()
	winning_boards = {}
	winning_board = []
	for number in numbers:
		board_pos = 0
		for board_pos in range(len(boards)):
			marked_board = mark_winners_in_board(boards[board_pos], number)
			boards[board_pos] = marked_board
			if check_if_board_is_winner(marked_board):
				if board_pos not in winning_boards:
					winning_boards[board_pos] = marked_board
					winning_board = marked_board
					if len(winning_boards) == len(boards):		
						sum_unmarked = 0
						for row in range(len(winning_board)):
							for col in range(len(winning_board)):
								if winning_board[row][col] != "x":
									sum_unmarked += int(winning_board[row][col])
						print(sum_unmarked * int(number))
						return True

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()