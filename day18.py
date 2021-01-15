

filename = "input_day18.txt"
testfile = "test_day18.txt"

def parse(file):
    infile = open(file, 'r').read().splitlines()

    return infile

def part1(file):
    answers = []
    for line in file:
        new_line = ""+line
        switch = True
        while(switch):
            temp = clear_parenth(new_line)
            new_line = temp[0]
            switch = temp[1]
        answers.append(int(evaluate(new_line)))
    return sum(answers)

def clear_parenth(line = ""):
    '''
    clears a parentheses in the line
    '''
    parenth = ""
    mem = False
    for char in line:
        if mem == True:
            parenth+=char
        if char == '(':
            if mem == True:
                parenth = ""
            mem = True    
        if char == ')':
            break
    if parenth == "":
        return line,False
    else:
        inside = evaluate(parenth[:-1])
        index = line.find(parenth)-1
        new_line =line[:index] + inside + line[index+len(parenth)+1:]
        return new_line,True
    


def evaluate(line):
    '''
    evaluate line from left to right
    no parentheses
    '''
    expressions = line.split()
    temp1 = 0
    temp2 = 0
    ans = 0
    sign = "add"
    for entry in expressions:
        if entry == "+":
            sign = "add"
        elif entry == "*":
            sign = "mult"
        else:
            #number
            if sign == "add":
                ans+=int(entry)
            else:
                ans*=int(entry)
    return str(ans)

def part2(file):
    answers = []
    for line in file:
        new_line = ""+line
        switch = True
        while(switch):
            temp = clear_parenth_new(new_line)
            new_line = temp[0]
            switch = temp[1]
        answers.append(int(evaluate_new(new_line)))
    return sum(answers)

def clear_parenth_new(line = ""):
    '''
    clears a parentheses in the line
    '''
    parenth = ""
    mem = False
    for char in line:
        if mem == True:
            parenth+=char
        if char == '(':
            if mem == True:
                parenth = ""
            mem = True    
        if char == ')':
            break
    if parenth == "":
        return line,False
    else:
        inside = evaluate_new(parenth[:-1])
        index = line.find(parenth)-1
        new_line =line[:index] + inside + line[index+len(parenth)+1:]
        return new_line,True

def evaluate_new(line):
    expression = line.split()

    while(add(expression)):
        1
    ans = 1
    for entry in expression:
        if entry !='*':
            ans*=int(entry)
    return str(ans)
def add(expression = []):
    '''
    perform the first instence of addition in the line
    '''
    for i in range(len(expression)):
        if expression[i] == '+':
            temp1= expression[i-1]
            temp2= expression[i+1]
            expression[i] = str(int(temp1)+int(temp2))
            expression.pop(i+1)
            expression.pop(i-1)
            return True
    return False

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
