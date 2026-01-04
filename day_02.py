# read input
input: list = list()
with open("input/day_02_input.txt") as file:
    for line in file:
        input.append(line.strip())

# Test-input
# input = """ULL
# RRDDD
# LURDL
# UUUUD""".split("\n")


def clamp(value, min_val=0, max_val=2):
    return max(min(value, max_val), min_val)


# 3x3 grid
x_coordinate = 1
y_coordinate = 1

keypad_dict: dict = {(0, 0): 1, (1, 0): 2, (2, 0): 3,
                     (0, 1): 4, (1, 1): 5, (2, 2): 6,
                     (0, 2): 7, (1, 2): 8, (2, 2): 9}

numbers: str = str()


for instructions in input:
    for instruction in instructions:
        match instruction:
            case "L":
                x_coordinate = clamp(x_coordinate-1)
            case "R":
                x_coordinate = clamp(x_coordinate+1)
            case "U":
                y_coordinate = clamp(y_coordinate-1)
            case "D":
                y_coordinate = clamp(y_coordinate+1)
    numbers += str(keypad_dict[(x_coordinate, y_coordinate)])
    # break

print(int(numbers))

# autopep8: off
keypad_dict:dict = {                         (2,0) : 1,                        
                                (1,1) : 2,   (2,1) : 3,   (3,1) : 4,           
                    (0,2) : 5,  (1,2) : 6,   (2,2) : 7,   (3,2) : 8, (4,2) : 9,
                                (1,3) : "A", (2,3) : "B", (3,3) : "C",         
                                             (2,4) : "D"}                      
# autopep8: on
# 5x5 grid
x_coordinate = 0
y_coordinate = 2
numbers = str()
for instructions in input:
    for instruction in instructions:
        match instruction:
            case "L":
                new_position: tuple = (x_coordinate-1, y_coordinate)
                if new_position in keypad_dict:
                    x_coordinate -= 1
            case "R":
                new_position: tuple = (x_coordinate+1, y_coordinate)
                if new_position in keypad_dict:
                    x_coordinate += 1
            case "U":
                new_position: tuple = (x_coordinate, y_coordinate-1)
                if new_position in keypad_dict:
                    y_coordinate -= 1
            case "D":
                new_position: tuple = (x_coordinate, y_coordinate+1)
                if new_position in keypad_dict:
                    y_coordinate += 1
    numbers += str(keypad_dict[(x_coordinate, y_coordinate)])


print(numbers)
