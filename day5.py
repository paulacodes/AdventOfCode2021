def part1():
	with open('inputs/day5.txt') as f:
		covered_coordinates = {}
		for line in f:
			coordinates = line.rstrip().split(" -> ")
			x1, y1 = coordinates[0].split(",")
			x2, y2 = coordinates[1].split(",")
			if x1 == x2:
				if int(y2) > int(y1):
					for i in range(int(y1), int(y2)+1):
						coordinate = x1 + "," + str(i)
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
				else:
					for i in range(int(y2), int(y1)+1):
						coordinate = x1 + "," + str(i)
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
			elif y1 == y2:
				if int(x2) > int(x1):
					for i in range(int(x1), int(x2)+1):
						coordinate = str(i) + "," + y2
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
				else:
					for i in range(int(x2), int(x1)+1):
						coordinate = str(i) + "," + y2
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
		overlaps = 0
		for coordinate in covered_coordinates:
			if covered_coordinates[coordinate] >= 2:
				overlaps += 1
		print(overlaps)

def part2():
	with open('inputs/day5.txt') as f:
		covered_coordinates = {}
		for line in f:
			coordinates = line.rstrip().split(" -> ")
			x1, y1 = coordinates[0].split(",")
			x2, y2 = coordinates[1].split(",")
			if x1 == x2:
				if int(y2) > int(y1):
					for i in range(int(y1), int(y2)+1):
						coordinate = x1 + "," + str(i)
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
				else:
					for i in range(int(y2), int(y1)+1):
						coordinate = x1 + "," + str(i)
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
			elif y1 == y2:
				if int(x2) > int(x1):
					for i in range(int(x1), int(x2)+1):
						coordinate = str(i) + "," + y2
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
				else:
					for i in range(int(x2), int(x1)+1):
						coordinate = str(i) + "," + y2
						if coordinate in covered_coordinates:
							covered_coordinates[coordinate] += 1
						else:
							covered_coordinates[coordinate] = 1
			elif int(x1) > int(x2) and int(y1) < int(y2):
				y_pos = int(y1)
				for row in range(int(x1), int(x2) - 1, - 1):
					coordinate = str(row) + "," + str(y_pos)
					if coordinate in covered_coordinates:
						covered_coordinates[coordinate] += 1
					else:
						covered_coordinates[coordinate] = 1
					y_pos += 1
			elif int(x1) < int(x2) and int(y1) < int(y2):
				y_pos = int(y1)
				for row in range(int(x1), int(x2) + 1):
					coordinate = str(row) + "," + str(y_pos)
					if coordinate in covered_coordinates:
						covered_coordinates[coordinate] += 1
					else:
							covered_coordinates[coordinate] = 1
					y_pos += 1
			elif int(x1) > int(x2) and int(y1) > int(y2):
				y_pos = int(y1)
				for row in range(int(x1), int(x2) - 1, - 1):
					coordinate = str(row) + "," + str(y_pos)
					if coordinate in covered_coordinates:
						covered_coordinates[coordinate] += 1
					else:
							covered_coordinates[coordinate] = 1
					y_pos -= 1
			elif int(x1) < int(x2) and int(y1) > int(y2):
				y_pos = int(y1)
				for row in range(int(x1), int(x2) + 1):
					coordinate = str(row) + "," + str(y_pos)
					if coordinate in covered_coordinates:
						covered_coordinates[coordinate] += 1
					else:
							covered_coordinates[coordinate] = 1
					y_pos -= 1
		overlaps = 0
		for coordinate in covered_coordinates:
			if covered_coordinates[coordinate] >= 2:
				overlaps += 1
		print(overlaps)


if __name__ == "__main__":
	print("Part 1:")
	part1()
	print("\nPart 2:")
	part2()
	