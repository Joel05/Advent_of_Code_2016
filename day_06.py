input:list = list()
with open("input/day_06_input.txt") as file:
    for line in file:
        input.append(line.strip())

#Testinput
# input = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar""".split()

common_dict_list:dict = [dict() for _ in range(len(input[0]))]

for line in input:
    for column, character in enumerate(line):
        if character in common_dict_list[column]:
            common_dict_list[column][character] += 1
        else:
            common_dict_list[column][character] = 1


solution_string: str = str()
for column in common_dict_list:
    solution_string += (sorted(column.items(), key= lambda x:x[1], reverse=False)[0][0])
    print(column)

print(solution_string)