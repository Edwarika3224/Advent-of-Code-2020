

filename = "input_day21.txt"
testfile = "test_day21.txt"

def parse(file):
    infile = open(file, 'r').read().splitlines()
    lines = []
    for line in infile:
        temp = line.split('(')
        ing = temp[0].split()
        alg = temp[1][8:-1].split(',')
        lines.append((ing,alg))
    return lines


def part1(file):
    allergens = get_names(file)
    bad = allergens.values()
    strings = []
    for entry in bad:
        for str1 in entry:
            strings.append(str1)
    safe_count = 0
    for food in file:
        for ingredient in food[0]:
            if ingredient not in strings:
                safe_count+=1
    return safe_count
    

def get_names(array = [()]):
    allergens = [] #list of all allergens
    for food in array:
        for alg in food[1]:
            if alg not in allergens:
                allergens.append(alg)

    alg_map = {}
    for alg in allergens:
        possible = [] #list of possible ingredients
        for food in array:
            if alg in food[1]:
                possible = common(food[0],possible)
        alg_map[alg] = possible

    return alg_map

def common(list1 = [], list2 = []):
    if list2 == []:
        return list1
    same = []
    for ingredient in list2:
        if ingredient in list1:
            same.append(ingredient)
    return same



def part2(file):
    allergens = determine_allergen(get_names(file))
    keys = allergens.keys()
    keys = sorted(keys)
    answer = []
    for alg in keys:
        answer.append(allergens[alg])
    return answer

    
def determine_allergen(dictionary = dict()):
    new_dict = dict()
    for entry in dictionary:
        if len(dictionary[entry]) ==1:
            new_dict[entry] = dictionary[entry][0]
    for entry in new_dict:
        dictionary.pop(entry)
    while(sort(new_dict,dictionary)):
        continue
    return new_dict

def sort(new_dict, dictionary):
    known = list(new_dict.values())
    changed = False
    for entry in dictionary:
        temp = []
        for ing in dictionary[entry]:
            if ing not in known:
                temp.append(ing)
        if len(temp) == 1:
            new_dict[entry] = temp[0]
            changed = True
    if changed:
        for entry in new_dict:
            dictionary.pop(entry,None)
    return changed
    
    

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
