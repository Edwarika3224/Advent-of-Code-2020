import string
import re

filename = "input_day19.txt"
testfile = "test_day19.txt"

def parse(file):
    infile = open(file, 'r')

    groups = infile.read().split('\n\n')
    rules = groups[0].split('\n')
    messages = groups[1].split('\n')

    infile.close()
    return rules,messages

def part1(file):

    rule_0 = decode_rules(file[0])
    correct = 0

    for message in file[1]:
        if message in rule_0:
            correct+=1
    return correct


def decode_rules(file):
    rules = {}
    for line in file:
        temp = line.split(': ')
        rules[temp[0]] = temp[1].strip('""')
    decoded = {}
    rule_0 = decode('0',rules,decoded)

    return rule_0

def decode(rule,rules = {}, decoded = {}):
    
    if rule in decoded:
        return decoded[rule]

    if rules[rule] in string.ascii_lowercase:
        decoded[rule] = [rules[rule]]
        return decoded[rule]

    #not a char not already decoded
    partition = rules[rule].split('|')
    this_rule = []
    for entry in partition:
        values = entry.split()
        lists = []
        for value in values:
            lists.append(decode(value,rules,decoded))
        this_rule.extend(combine(lists))

    return this_rule
        
def combine(lists = [[]]):
    combined = []
    length = len(lists)
    if length == 1:
        return lists[0]
    if length == 2:
        for str1 in lists[0]:
            for str2 in lists[1]:
                combined.append(str1+str2)
    elif length == 3:
        for str1 in lists[0]:
            for str2 in lists[1]:
                for str3 in lists[2]:
                    combined.append(str1+str2+str3)
    else:
        raise AssertionError("too many lists in list")
    return combined
   

def part2(file):

    rules = {}
    for line in file[0]:
        temp = line.split(': ')
        rules[temp[0]] = temp[1].strip('""')
    decoded = {}
    rule_42 = decode('42',rules,decoded)
    rule_31 = decode('31',rules,decoded)
    # rule 8 is rule42 any number of times
    # rule 11 is rule 42 x amount of times followed by rule 31 x amount of times
    # rule 0 is rule 8 followed by rule 11
    correct = 0
    for message in file[1]:
        for str1 in rule_42:
            try:
                if message.index(str1) == 0:
                    #starts with a string from rule42
                    new_string = message[len(str1):]
                
                    times_42 = 0
                    check_42 = True
                    while(check_42):
                        for str2 in rule_42:
                            try:
                                if new_string.index(str2) == 0:
                                    new_string = new_string[len(str2):]
                                    times_42+=1
                                    check_42 = True
                                    break
                                else:
                                    check_42 = False
                            except:
                                check_42 = False
                    if times_42 == 0:
                        break #invalid
                    
                    times_31 = 0
                    check_31 = True
                    while(check_31):
                        for str2 in rule_31:
                            try:
                                if new_string.index(str2) == 0:
                                    new_string = new_string[len(str2):]
                                    times_31+=1
                                    check_31 = True
                                    break
                                else:
                                    check_31 = False
                            except:
                                check_31 = False
                    if times_31 == 0:
                        break #invalid

                    #after checking both stings
                    if new_string == "":
                        if times_31 <= times_42:
                            correct+=1
            except:
                continue


    return correct


if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    print(part2(test_input))

    #print(part1(input))
    print(part2(input))
