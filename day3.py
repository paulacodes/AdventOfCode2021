def find_numbers_with_predominant_bit(position, numbers, type):
	zero_count = 0
	one_count = 0
	for number in numbers:
		if number[position] == "0":
			zero_count += 1
		else:
			one_count += 1
	if type == "oxygen":
		if zero_count > one_count:
			predominant_number = "0"
		else:
			predominant_number = "1"
	else:
		if zero_count > one_count:
			predominant_number = "1"
		else:
			predominant_number = "0"
	remaining_numbers = []
	for number in numbers:
		if number[position] == predominant_number:
			remaining_numbers.append(number)
	return remaining_numbers

def part1():
	zero_counts = {}
	one_counts = {}
	with open('inputs/day3.txt') as f:
		number = f.readline().rstrip()
		for i in range(len(number)):
			zero_counts[i] = 0
			one_counts[i] = 0
		for line in f:
			position = 0
			number = line.rstrip()
			for digit in number:
				if digit == "0":
					if position in zero_counts:
						zero_counts[position] += 1
				elif digit == "1":
					if position in one_counts:
						one_counts[position] += 1
				position += 1
	f.close()
	gamma = ""
	epsilon = ""
	for position in zero_counts:
		if zero_counts[position] > one_counts[position]:
			gamma += "0"
			epsilon += "1"
		else:
			gamma += "1"
			epsilon += "0"
	gamma_int = int(gamma, 2)
	epsilon_int = int(epsilon, 2)
	print(gamma_int * epsilon_int)

def part2():
	numbers = []
	with open('inputs/day3.txt') as f:
		for line in f:
			number = line.rstrip()
			numbers.append(number)
	f.close()
	oxygen_generator_numbers = numbers
	co2_scrubber_rating_numbers = numbers
	for position in range(len(numbers[0])):
		oxygen_generator_numbers = find_numbers_with_predominant_bit(position, oxygen_generator_numbers, "oxygen")
		if len(oxygen_generator_numbers) == 1:
			break
	for position in range(len(numbers[0])):
		co2_scrubber_rating_numbers = find_numbers_with_predominant_bit(position, co2_scrubber_rating_numbers, "co2")
		if len(co2_scrubber_rating_numbers) == 1:
			break
	oxygen_generator = int(oxygen_generator_numbers[0], 2)
	co2_scrubber_rating = int(co2_scrubber_rating_numbers[0], 2)
	print(oxygen_generator * co2_scrubber_rating)

if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()