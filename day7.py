from advent_of_code import openfile

filename = "input_day7.txt"
testfile = "test_day7.txt"
our_bag = "shiny gold"

def parse(file):
    '''
    conver the file into a list of bags within the file
    '''
    lines = file.read().split('.\n')
    bags = []
    for line in lines:
        line = line.split(' bags contain ')
        
        inner_bags = line[1].split(', ')
        if "no other" in inner_bags[0]:
            bags.append(bag(line[0],{}))
        else:
            temp_dictionary = {}
            for bag_code in inner_bags:
                if bag_code[-1] == 's':
                    bag_code = bag_code[:-5]
                else:
                    bag_code = bag_code[:-4]
                temp_dictionary.update({bag_code[2:]:int(bag_code[0])})
            bags.append(bag(line[0],temp_dictionary))
    return bags


def part1(bags):
    in_bag_outter = [] #list of outtermost bags we can be in
    in_bag = bags_containing(our_bag, bags)

    temp = ([], in_bag)
    while len(temp[1]) != 0:
        #exit when there are no new bags
        temp = check_bags(temp[1],bags)
        for entry in temp[0]:
            if entry not in in_bag_outter:
                in_bag_outter.append(entry)
        for entry in temp[1]:
            if entry not in in_bag:
                in_bag.append(entry)

    return len(in_bag)


def check_bags(check_bag, bags):
    '''
    input: a list of bag names to check in baglist
    return: bags which were the outtermost and new bags to be checked
    '''
    outtermost = []
    new_bags = []
    for bag_name in check_bag:
        temp_list = bags_containing(bag_name,bags)
        if  temp_list == []:
            #no bag contains bag
            outtermost.append(bag_name)
        else:
            #is in a bag
            for entry in temp_list:
                if entry not in check_bag and entry not in new_bags:
                    #new bags to be checked
                    new_bags.append(entry)
    return (outtermost,new_bags)

def bags_containing(my_bag,bag_list):
    '''
    my_bag is a string
    returns a list of bags containing my_bag
    '''
    in_bag = []
    for bag in bag_list:
        if bag.is_bag_in(my_bag):
            in_bag.append(bag.get_name())

    return in_bag


def part2(bags):

    #get the bag we want
    for entry in bags:
        if entry.get_name() == our_bag:
            this_bag = entry
            break

    return bags_inside(this_bag,bags,{})[0]

def bags_inside(bag,bags,mem):
    '''
    bag: bag object to be checked
    bags: list of all bags
    mem: bags we know the answer for
    returns: (number of bags contained, memory)
    '''
    num_inside = 0
    in_bag = bag.get_inner_bags()
    if len(in_bag) == 0:
        return (0,mem)
    if bag.get_name() in mem:
        return (mem[bag.get_name()],mem)
    for name in in_bag.keys():
        for entry in bags:
            if name == entry.get_name():
                that_bag = entry
                break
        temp = bags_inside(that_bag,bags,mem) #number of bags in that bag
        in_that_bag = temp[0]
        mem.update(temp[1])
        mem.update({name:in_that_bag}) #update memory with the entry we used
        
        num_inside += in_bag[name] + in_bag[name]*in_that_bag #add to total number of bags in this entire bag
        


    return (num_inside, mem)


class bag(object):
    def __init__(self, name, inner_bags):
        self.outer_bag = name
        self.inner_bags = inner_bags
    def get_name(self):
        return self.outer_bag
    def get_inner_bags(self):
        return self.inner_bags
    def is_bag_in(self, bag_name):
        return bag_name in self.inner_bags


if __name__ == "__main__":
    test_input = parse(openfile(testfile))
    input = parse(openfile(filename))

    print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
