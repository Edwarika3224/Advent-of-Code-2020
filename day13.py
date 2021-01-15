

filename = "input_day13.txt"
testfile = "test_day13.txt"

def parse(file):
    infile = open(file, 'r').read().splitlines()

    earliest = int(infile[0])
    busses = infile[1].split(',')
    bus = []
    for entry in busses:
        if entry != 'x':
            bus.append(int(entry))
    return [earliest,bus]

def part1(file):
    earliest = file[0]
    temp = 0
    for bus in file[1]:
        if earliest%bus > temp:
            temp = bus
    return (temp-earliest%temp)*temp
    
def parse2(file):
    infile = open(file, 'r').read().splitlines()
    buss = infile[1].split(',')
    constraints = {}
    for i in range(len(buss)):
        if buss[i] !='x':
            constraints[buss[i]] = i


    return constraints

def part2(file):
    #13 and 449
    #37 and 773

    dif = file['773'] - file['449']
    i = 1
    m = 1
    while(True):
        temp1 = 13*449*i
        temp2 = 37*773*m
        if temp1+dif == temp2:
            if check_contraints(temp1,temp2,file):
                break
            i+=1
            m+=1
            
        elif temp1-temp2 > 37*773:
            m+=1
        elif temp2-temp1 > 37*773:
            i+=1
        else:
            i+=1
            m+=1
    return temp1-13

def part2_try2(file):
    #13 449 19 41 23 all lie on the same position
    #37 773 29 17 
    dif = file['773'] - file['449']
    i = 1
    m = 1
    Switch = True
    while(Switch):
        temp1 = 23*449*i
        temp2 = 41*m
        if temp1 == temp2:
            if (temp1)%13 == 0:
                if (temp1)%19 == 0:
                    if (temp1)%41 == 0:
                        break
            i+=1
            m+=1
            
        elif temp1-temp2 > 41:
            m+=1
        elif temp2-temp1 > 41:
            i+=1
        else:
            i+=1
            m+=1
    return
def check_contraints(temp1,temp2,file):

    if (temp1+2)%29 == 0:
        if (temp1+19)%19 ==0:
            if (temp2+10)%41 ==0:
                if (temp2+17)%17 == 0:
                    return True
    return False

def part2_test(file):
    #7 and 19

    dif = -1

    i = 1
    m = 1
    Switch = True
    while(Switch):
        temp1 = 7*19*i
        temp2 = 31*m
        if temp1+dif == temp2:
            if (temp1-3)%59 == 0:
                if (temp1-6)%13 == 0:
                    break
            i+=1
            m+=1
            
        elif temp1-temp2 > 31:
            m+=1
        elif temp2-temp1 > 31:
            i+=1
        else:
            i+=1
            m+=1
    return
            




if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    #print(part2(test_input))

    print(part1(input))

    #part2_test(parse2(testfile))
    input = parse2(filename)
    print(part2_try2(input))
