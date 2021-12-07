import statistics

def part1():
	with open('inputs/day7.txt') as f:
		positions = list(map(int,f.readline().rstrip().split(",")))
	f.close()
	median = statistics.median(positions)
	fuel_total = 0
	for position in positions:
		fuel_total += abs(position-median)
	print(int(fuel_total))

def part2():
	with open('inputs/day7.txt') as f:
		positions = list(map(int,f.readline().rstrip().split(",")))
	f.close()
	min_position = min(positions)
	max_position = max(positions)
	cost_per_option = {}
	for option in range(min_position, max_position):
		total_fuel = 0
		for position in positions:
			distance = abs(position-option)
			total = distance * (distance + 1)/2
			total_fuel += total
		cost_per_option[option] = total_fuel
	print(int(min(zip(cost_per_option.values(), cost_per_option.keys()))[0]))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()
	