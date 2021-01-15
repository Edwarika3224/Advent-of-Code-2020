import numpy

filename = "input_day9.txt"
testfile = "test_day9.txt"

def parse(file):
    infile = open(file, 'r')

    lines = infile.read().splitlines()

    infile.close()
    ints = []
    for i in range(len(lines)):
        ints.append(int(lines[i]))
    return ints

def part1(file):

    for i in range(25,len(file)):
        if not valid(file[i-25:i+1]):
            return file[i]
    pass

def valid(array):

    for i in range(len(array)-1):
        times = 0
        for n in range(len(array)-1):
            if array[n] == array[i] and times == 0:
                times+=1
            else:
                if array[-1] == array[i] + array[n]:
                    return True
    return False


def part2(file):

    invalid = part1(file)
    for i in range(len(file)):
        sum = 0
        for n in range(i,len(file)):
            sum+=file[n]
            if sum == invalid:
                return large_small(file[i:n+1])
            if sum>invalid:
                break
    raise AssertionError

def large_small(array):
    sorted = array.sort()
    return array[0]+array[-1]

if __name__ == "__main__":

    #test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    #print(part2(test_input))

    print(part1(input))
    print(part2(input))
