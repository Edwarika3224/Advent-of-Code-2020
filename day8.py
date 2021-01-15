

filename = "input_day8.txt"
testfile = "test_day8.txt"

def parse(file):
    '''
    Returns the file as a list of lists
    where the inner list is the command and it's value
    '''
    infile = open(file, 'r')

    input = []
    for line in infile:
        input.append(line.split())

    infile.close()
    return input

def part1(file):
    '''
    input: a list of commands
    returns: the acc value before the loop
    '''
    acc = 0
    lines_visited = []
    i=0
    while(True):
        if i in lines_visited:
            break
        lines_visited.append(i)
        if file[i][0] == 'acc':
            if file[i][1][0] =='-':
                acc -= int(file[i][1][1:])
            else:
                acc += int(file[i][1][1:])
        elif file[i][0] == 'jmp':
            if file[i][1][0] =='-':
                i-= int(file[i][1][1:])+1
            else:
                i+= int(file[i][1][1:])-1
        i+=1
    return acc

def part2(file):
    '''
    Tries every possible command change until a non looping command list is provided

    input: a list of commands
    returns: the fixed list
    '''
    for i in range(len(file)):
        if file[i][0] == 'jmp':
            file[i][0] = 'nop'
            if check_loop(file):
                file[i][0] = 'jmp' #revert change
            else:
                return file #file that doesn't loop
        elif file[i][0] == 'nop':
            file[i][0] = 'jmp'
            if check_loop(file):
                file[i][0] = 'nop' #revert change
            else:
                return file #file that doesn't loop

    raise ArithmeticError

def check_loop(file):
    '''
    returns: True if the commands loop
             False otherwise
    '''
    lines_visited = []
    i=0
    while(True):
        try:
            if i in lines_visited:
                return True
            lines_visited.append(i)
            if file[i][0] == 'jmp':
                if file[i][1][0] =='-':
                    i-= int(file[i][1][1:])+1
                else:
                    i+= int(file[i][1][1:])-1
            i+=1
        except:
            return False
    raise ArithmeticError

def get_acc_value(file):
    '''
    input: a list of commands that do not loop
    return: the proper acc value after  going through the command list
    '''
    acc = 0
    lines_visited = []
    i=0
    while(True):
        try: 
            file[i]
        except:
            return acc
        if i in lines_visited:
            break
        lines_visited.append(i)
        if file[i][0] == 'acc':
            if file[i][1][0] =='-':
                acc -= int(file[i][1][1:])
            else:
                acc += int(file[i][1][1:])
        elif file[i][0] == 'jmp':
            if file[i][1][0] =='-':
                i-= int(file[i][1][1:])+1
            else:
                i+= int(file[i][1][1:])-1
        i+=1
    raise ArithmeticError


if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    print(get_acc_value(part2(test_input)))

    #print(part1(input))
    print(get_acc_value(part2(input)))
