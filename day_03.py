# read input
input: list = list()
with open("input/day_03_input.txt") as file:
    for line in file:
        input.append(line.strip())

solution = 0

for triangle in input:
    side_a, side_b, side_c = map(int, triangle.split())
    if (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a:
        solution += 1

print(solution)


solution = 0
for index in range(0, len(input), 3):
    lines: list = input[index:index+3]
    triangles:list = [[None for _ in range(3)] for _ in range(3)]
    for side_index, line in enumerate(lines):
        for triangle_index in range(3):
            triangles[triangle_index][side_index] = line.split()[triangle_index]
    for triangle in triangles:
        side_a, side_b, side_c = map(int, triangle)
        if (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a:
            solution += 1

print(solution)