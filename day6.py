from advent_of_code import openfile
import string

filename = "input_day6.txt"
testfile = "test_day6.txt"

def parse(file):

    pass

def part1(file):
    index = []
    group = ""
    for line in file:
        if line != "\n":
            group+= line[:-1]
        else:
            index.append(group_count(group))
            group = ""
    return sum(index)
    

def part2(file):
    index = []
    group = []
    for line in file:
        if line != "\n":
            group.append(line[:-1])
        else:
            index.append(group_same(group))
            group.clear()
    return sum(index)


def group_count(group_answers):
        '''
        input: string of entries concatinated
        return number questions answered yes
        '''
        count = 0
        for char in string.ascii_lowercase:
            if char in group_answers:
                count+=1
        return count

def group_same(group_answers):
    '''
    input: array of grou_answers
    return: number of same ansawers
    '''
    same= 0
    if group_answers == []:
        return 0
    for char in string.ascii_lowercase:
        if all(char in group_answers[i] for i in range(len(group_answers))):
               same+=1
    return same
if __name__ == "__main__":

    #print(part1(openfile(testfile)))
    print(part2(openfile(testfile)))

    #print(part1(openfile(filename)))
    print(part2(openfile(filename)))
