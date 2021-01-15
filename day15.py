import time

filename = "input_day15.txt"
testfile = "test_day15.txt"

def parse(file):
    infile = open(file, 'r')

    array = list(map(int, infile.read().split(',')))

    infile.close()
    return array

def part1(file):
    said = set(file)
    num = []
    num.extend(file)
    num.append(0)

    for i in range(len(file), 2020):
        if num[-1] in said:
            for n in range(len(num)):
                if num[-2-n] == num[-1]:
                    num.append(n+1)
                    break
        else:
            said.add(num[-1])
            num.append(0)         
    return num[-2]


def part2_try1(file):
    said = set(file)
    num = []
    num.extend(file)
    num.append(0)

    for i in range(len(file), 30000000):
        if num[-1] in said:
            for n in range(len(num)):
                if num[-2-n] == num[-1]:
                    num.append(n+1)
                    break
        else:
            said.add(num[-1])
            num.append(0)         
    return num[-2]

def part2(file):
    said = dict()
    i = 1
    for index in file:
        said[index] = i
        i+=1
    value = 0

    for i in range(i,30000000):
        try:
            temp = said[value]
            said[value] = i
            value = i-temp
        except:
            said[value] = i
            value = 0
    return value
                
if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    start = time.time()
    print(part2(test_input))
    end = time.time()
    print("runtime = ", end-start)

    print(part1(input))
    start = time.time()
    print(part2(input))
    end = time.time()
    print("runtime = ", end-start)
