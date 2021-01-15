import re
import numpy as np

filename = "input_day14.txt"
testfile = "test_day14.txt"

def parse(file):
    return open(file, 'r').read().splitlines()


def part1(file):
    mask = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    mem  = dict()
    for line in file:
        if line[:4] == 'mask':
            mask = line[7:]
        else:
            line = re.findall(r'\d+', line)
            mem[line[0]] = convert(mask,int(line[1]))


    return sum(mem.values())
def convert(mask, value):
    binary = f'{value:036b}'
    new_value = ""

    for i in range(36):
        if mask[i] == 'X':
            new_value+=binary[i]
        elif mask[i] == '1':
            new_value+='1'
        else:
            new_value+='0'
    return int(new_value,2)
            
def part2(file):
    mask = ''
    mem = dict()
    add_list = []
    permutations = set() #num of x's in a mash
    for line in file:
        if line[:4] == 'mask':
            mask = line[7:]
            permutations = perm(mask.count('X'))
        else:
            line = re.findall(r'\d+', line)
            add_list = get_add(mask, int(line[0]), permutations)
            for address in add_list:
                mem[address] = int(line[1])

    return sum(mem.values())

def perm(num):
    values = set()
    for i in range(2**num):
        values.add(np.binary_repr(i,width = num))
    return values

def get_add(mask, value, permutations):
    binary = f'{value:036b}'
    new_add = ""
    add_list = set()
    for i in range(36):
        if mask[i] == 'X':
            new_add+='X'
        elif mask[i] == '1':
            new_add+='1'
        else:
            new_add+=binary[i]
    for entry in permutations:
        add_list.add(impose(entry,new_add))
    return add_list

def impose(value,address):
    i = 0
    new_add = ""
    for char in address:
        if char == 'X':
            new_add += value[i]
            i+=1
        else:
            new_add += char
    return new_add

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
