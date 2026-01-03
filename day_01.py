
# read input
with open("input/day_01_input.txt") as file:
    input = file.readline()

### Test-input
#input = "R8, R4, R4, R8"


east_distance = 0
north_distance = 0

headings = ("north", "east", "south", "west")

#current heading can be 0-3
current_heading = 0

visited_locations:set = set()
visited_locations.add((0,0))

location_found = False

for instruction in input.split(", "):
    distance = int(instruction[1:])
    if instruction[0] == "R":
        current_heading = (current_heading + 1)%4
    elif instruction[0] == "L":
        current_heading = (current_heading + 3)%4
    for _ in range(distance):
        match current_heading:
            case 0:
                north_distance += 1
            case 1:
                east_distance += 1
            case 2:
                north_distance -= 1
            case 3:
                east_distance -= 1  
        if tuple((east_distance, north_distance)) in visited_locations:
            visited_locations.add((east_distance, north_distance))
            location_found = True
            break
        visited_locations.add((east_distance, north_distance))
    if location_found:
        break
print(abs(north_distance) + abs(east_distance))
#print(visited_locations)