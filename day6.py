import copy

def get_fish_count_after_n_days(days):
	with open('inputs/day6.txt') as f:
		ages = list(map(int,f.readline().rstrip().split(",")))
		age_mappings = {}
		for age in range(9):
			age_mappings[age] = 0
		for age in ages:
			age_mappings[age] += 1
		for i in range(days):
			new_age_mappings = copy.deepcopy(age_mappings)
			for age in age_mappings.keys():
				if age == 0:
					new_age_mappings[6] += age_mappings[0]
					new_age_mappings[8] += age_mappings[0]
					new_age_mappings[age] -= age_mappings[age]
				else:
					new_age_mappings[age-1] += age_mappings[age]
					new_age_mappings[age] -= age_mappings[age]
			age_mappings = copy.deepcopy(new_age_mappings)
		total_fish = 0
		for age in age_mappings:
			total_fish += age_mappings[age]
		return(total_fish)

def part1():
	print(get_fish_count_after_n_days(80))

def part2():
	print(get_fish_count_after_n_days(256))

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()
	