
import string
import pylab

def open_file(filename):
    infile = open(filename, 'r')
    correct = 0
    for line in infile:
        apparence = 0
        temp = line.split()
        number = temp[0].split('-')
        temp[1] = temp[1].strip(':')
        temp[1] = temp[1].strip("\n")
        for entry in temp[2]:
            if temp[1] == entry:
                apparence+=1
        if apparence >= int(number[0]) and apparence <= int(number[1]):
            correct+=1
    infile.close()
    return correct

def part2(filename):
    infile = open(filename, 'r')
    correct = 0
    for line in infile:
        apparence = 0
        temp = line.split()
        number = temp[0].split('-')
        temp[1] = temp[1].strip(':')
        temp[1] = temp[1].strip("\n")
        if temp[2][int(number[0])-1] == temp[1]:
            if temp[2][int(number[1])-1] != temp[1]:
                #valid, only in 1st spot
                correct+=1
        elif temp[2][int(number[1])-1] == temp[1]:
            #in second spot
            correct+=1
    infile.close()
    return correct

if __name__ == "__main__":
    print(part2("input_day2.txt"))
    end