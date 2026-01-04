import hashlib

input:list = list()
with open("input/day_05_input.txt") as file:
    for line in file:
        input.append(line.strip())

#Testinput
# input = "abc".split()


def task1():
    solution_string:str = str()
    for index in range(10000000000):
        md5_input:str = input[0] + str(index)
        hashed = hashlib.md5(md5_input.encode()).digest().hex()
        last_5_digits = hashed[:5]
        if last_5_digits == "00000":
            solution_string += hashed[5]
        if len(solution_string) == 8:
            break
    return solution_string

def task2():
    solution_list:list = [None for _ in range(8)]
    solution_string:str = str()
    for index in range(10000000000):
        md5_input:str = input[0] + str(index)
        hashed = hashlib.md5(md5_input.encode()).digest().hex()
        last_5_digits = hashed[:5]
        if last_5_digits == "00000":
            if hashed[5].isnumeric():
                if int(hashed[5]) < 8:
                    if solution_list[int(hashed[5])] is None:
                        solution_list[int(hashed[5])] = hashed[6]
                        print(hashed[6], "in position", hashed[5])
                        if None not in solution_list:
                            break
    for character in solution_list:
        solution_string += str(character)

    return solution_string

print(task2())