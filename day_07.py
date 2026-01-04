import re

input: list = list()
with open("input/day_07_input.txt") as file:
    for line in file:
        input.append(line.strip())

# Testinput - True False False True
# input = """abba[mnop]qrst
# abcd[bddb]xyyx
# aaaa[qwer]tyui
# ioxxoj[asdfgh]zxcvbn
# vddqfnrfmbxrayhmfph[dbsadhdnaweddhn]fvwaseggzyqhybmbdxr[brelmqesxjfgkkyyufr]acdmphljtmdqbed""".split()

def task1():
    solution:int = 0
    for network in input:
        #print(network)
        networks =  re.findall("(?:^|(?<=\]))[^[]+(?=\[|$)", network)
        hypernets = re.findall("(?<=\[)[^\]]+(?=\])",network)
        network_is_abba = False
        hypernet_is_abba = False
        
        for network_index in range(len(networks)):
            for index in range(len(networks[network_index])-3):
                network_subnet = networks[network_index][index:index+4]
                if network_subnet[0:2] == network_subnet[-1:1:-1] and network_subnet[0] is not network_subnet[1]:
                    network_is_abba = True
                
        for hypernet_index in range(len(hypernets)):
            for index in range(len(hypernets[hypernet_index])-3):
                hypernet_subnet = hypernets[hypernet_index][index:index+4]
                if hypernet_subnet[0:2] == hypernet_subnet[-1:1:-1] and hypernet_subnet[0] is not hypernet_subnet[1]:
                    hypernet_is_abba = True
        if (network_is_abba is True) and not hypernet_is_abba:
            solution += 1
    return solution

#print(task1())



def task2():
    solution:int = 0
    for network in input:
        networks =  re.findall("(?:^|(?<=\]))[^[]+(?=\[|$)", network)
        hypernets = re.findall("(?<=\[)[^\]]+(?=\])",network)
        network_is_aba = False
        hypernet_is_bab = False
        
        for network_index in range(len(networks)):
            for index in range(len(networks[network_index])-2):
                network_subnet = networks[network_index][index:index+3]
                if network_subnet[0] == network_subnet[-1] and network_subnet[0] != network_subnet[1]:
                    network_is_aba = True
                
                for hypernet_index in range(len(hypernets)):
                    for index in range(len(hypernets[hypernet_index])-2):
                        hypernet_subnet = hypernets[hypernet_index][index:index+3]
                        if (network_subnet[0] == hypernet_subnet[1] and 
                            network_subnet[1] == hypernet_subnet[0] and
                            network_subnet[1] == hypernet_subnet[2] and
                            network_subnet[2] == hypernet_subnet[1]):
                            hypernet_is_bab = True
        if network_is_aba and hypernet_is_bab:
            solution += 1
    return solution


print(task2())