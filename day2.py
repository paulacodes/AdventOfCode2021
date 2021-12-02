def part1():
	h_start = 0
	d_start = 0
	with open('inputs/day2.txt') as f:
		for line in f:
			instruction = line.rstrip()
			direction = instruction.split(" ")[0]
			steps = int(instruction.split(" ")[1])
			if direction == "forward":
				h_start += steps
			elif direction == "down":
				d_start += steps
			elif direction == "up":
				d_start -= steps
	f.close()
	print(h_start*d_start)

def part2():
	h_start = 0
	d_start = 0
	aim = 0
	with open('inputs/day2.txt') as f:
		for line in f:
			instruction = line.rstrip()
			direction = instruction.split(" ")[0]
			steps = int(instruction.split(" ")[1])
			if direction == "forward":
				h_start += steps
				d_start += aim * steps
			elif direction == "down":
				aim += steps
			elif direction == "up":
				aim -= steps
	f.close()
	print(h_start*d_start)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()