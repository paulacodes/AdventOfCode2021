def part1():
	numbers = []
	greater_than = 0
	with open('inputs/day1.txt') as f:
		current_number = int(f.readline().rstrip())
		for line in f:
			next_number = int(line.rstrip())
			if next_number > current_number:
				greater_than += 1
			current_number = next_number
			numbers.append(int(line.rstrip()))
	f.close()
	print(greater_than)

def part2():
	windows = {}
	numbers = []
	with open('inputs/day1.txt') as f:
		for line in f:
			numbers.append(int(line.rstrip()))
	f.close()
	total_windows = len(numbers) - 2
	greater_than = 0
	current_window = numbers[0] + numbers[1] + numbers[2]
	for i in range(total_windows):
		windows[i] = numbers[i] + numbers[i+1] + numbers[i+2]
		if windows[i] > current_window:
			greater_than += 1
		current_window = windows[i]
	print(greater_than)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()