import re

filename = "input_day16.txt"
testfile = "test_day16.txt"

def parse(file):
    infile = open(file, 'r')

    groups = infile.read().split('\n\n')
    rules = {}
    for line in groups[0].split('\n'):
        #rules
        ints = re.findall(r'\d+',line)
        field = line.split(':')[0]
        rules[field] = set()
        for i in range(int(ints[0]),int(ints[1])+1):
            rules[field].add(i)
        for i in range(int(ints[2]),int(ints[3])+1):
            rules[field].add(i)

    my_ticket = groups[1].split('\n')[1]
    tickets = groups[2].split('\n')[1:-1]
    infile.close()
    return (rules, my_ticket, tickets)

def part1(file):
    rules = file[0]
    tickets = file[2]
    
    errors = []

    for line in tickets:
        ticket = line.split(',')
        for value in ticket:
            if all([int(value) not in range for range in rules.values()]):
                errors.append(int(value))

    return sum(errors)

def part2(file):
    rules = file[0]
    my_ticket = file[1].split(',')
    tickets = [file[1]]
    tickets.extend(file[2])
    arangement = []
    
    for i in range(len(my_ticket)):
        possible_fields = set(rules.keys())
        for line in tickets:
            ticket = line.split(',')
            for field in rules.keys():
                if int(ticket[i]) not in rules[field]:
                    possible_fields.discard(field)
                    
        arangement.append(possible_fields)

    arangement = finalize(arangement)

    answer = []
    for i in range(len(arangement)):
        if "departure" in arangement[i]:
            answer.append(int(my_ticket[i]))

    temp = 1
    for entry in answer:
        temp*=entry
    return temp

def finalize(arangement):
    sort = [None] * len(arangement)
    Switch = True
    while(Switch):
        for i in range(len(arangement)):
            if len(arangement[i]) == 1:
                sort[i] = list(arangement[i])[0]
                for n in range(len(arangement)):
                    arangement[n].difference_update({sort[i]})
        if all([entry != None for entry in sort]):
            Switch = False

    return sort

def discard(file):
    rules = file[0]
    tickets = file[2]
    
    errors = []
    location = enumerate(tickets)

    for line in tickets:
        ticket = line.split(',')
        for value in ticket:
            if all([int(value) not in range for range in rules.values()]):
                errors.append(line)
                break
    for error in errors:
        tickets.remove(error)
    return (file[0],file[1],tickets)

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    test_input = discard(test_input)
    #print(part2(test_input))

    print(part1(input))
    input = discard(input)
    print(part2(input))
