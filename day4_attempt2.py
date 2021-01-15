from advent_of_code import openfile

filename = "input_day4_meep.txt"

def part1(filename):
    valid=0
    passport = {}
    for line in infile:
        if line != "\n":
            temp = (line.split())
            for entry in temp:
                entry = entry.split(':')
                passport.update({entry[0] : entry[1]})
        else:
            if is_passport_valid(passport):
                valid+=1
            passport.clear()
            

    return valid

def part2(filename):
    valid=0
    passport = {}
    for line in infile:
        if line != "\n":
            temp = (line.split())
            for entry in temp:
                entry = entry.split(':')
                passport.update({entry[0] : entry[1]})
        else:
            if is_passport_valid(passport) and is_cridentials_valid(passport):
                valid+=1
            passport.clear()
            

    return valid

def is_cridentials_valid(passport):
    valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    #birth year test
    if not 1920<=int(passport['byr'])<=2002:
        return False
    #issue year test
    if not 2010<=int(passport['iyr'])<=2020:
        return False
    #experation year test
    if not 2020<=int(passport['eyr'])<=2030:
        return False
    #height test
    height = passport['hgt']
    if "cm" == height[-2::]:
        if not 150<=int(height[:-2:])<=193:
            return False
    elif "in" == height[-2::]:
        if not 59<=int(height[:-2:])<=76:
            return False
    else:
        #invalid Height
        return False
    #hair color test
    if passport['hcl'][0] != '#':
        return False
    if len(passport['hcl']) != 7:
        return False
    for i in passport['hcl'][1::]:
                try: 
                    int(i)
                except: 
                    if i not in "abcdef":
                        return False
    #eye color test
    if passport['ecl'] not in valid_ecl:
        return False
    #passport id test
    if len(passport['pid']) != 9:
        return False
    try:
        int(passport['pid'])
    except:
        return False
    #pass all tests
    return True


def is_passport_valid(passport):
    '''
    input: a dictionary of entries
    return: true or false if valid
    '''

    return all(key in passport for key in ['byr','iyr','eyr','hgt','hcl','ecl','pid'])


if __name__ == "__main__":

    infile = openfile(filename)
    ans = part1(infile)
    #ans = part2(infile)

    print(ans)
    

