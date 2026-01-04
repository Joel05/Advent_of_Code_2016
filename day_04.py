# read input
input: list = list()
with open("input/day_04_input.txt") as file:
    for line in file:
        input.append(line.strip())

# # Test-input
# input = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]
# qzmt-zixmtkozy-ivhz-343[lol]""".split("\n")

solution = 0

replacement_map = str.maketrans("", "", "-1234567890[]")

def sorting_function(n):
    return n[0]

for line in input:
    string = line.split("[")[0].translate(replacement_map)
    sector_id = line.split("[")[0].split("-")[-1]
    checksum = line.split("[")[1].translate(replacement_map)
    count_dict:dict = dict()
    for character in string:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    real_checksum_dict = sorted(count_dict.items(), key=lambda x:(-x[1], x[0]))[:5]
    real_checksum_string = str()
    for checksum_part in real_checksum_dict:
        real_checksum_string += checksum_part[0]
    if real_checksum_string == checksum:
        solution += int(sector_id)
    
print(solution)

###task2
for line in input:
    string = line.split("[")[0].translate(replacement_map)
    sector_id = line.split("[")[0].split("-")[-1]
    checksum = line.split("[")[1].translate(replacement_map)
    name_string:str = str()
    for character in string:
        string_integer = ((ord(character) + int(sector_id)))
        if string_integer > 122:
            string_integer = ((string_integer - ord("a")) % 26) + 97
        name_string += chr(string_integer)
    if name_string == "northpoleobjectstorage":
        print(sector_id)