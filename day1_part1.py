


def sum_search(fin_report):
    '''
    takes in a list of ints and finds which two add to 2020
    returns: the two ints
    '''
    temp = 2020
    i = 1
    for int in fin_report:
        if int < 2020:
            temp = 2020 - int
            for n in range(i,len(fin_report)):
                if fin_report[n] == temp:
                    return (temp, 2020-temp)

        i+=1
    raise ArithmeticError
        
def open_file(filename):

    array = []
    infile = open(filename,'r')
    for line in infile:
        line = line.strip("\n")
        array.append(int(line))
    return array

def sum_search_three(fin_report):
    temp = 2020
    i = 1
    for int in fin_report:
        if int < 2020:
            for n in range (i,len(fin_report)):
                if int+fin_report[n] <2020:
                    for m in range(n+1,len(fin_report)):
                        if int+fin_report[n]+fin_report[m] == 2020:
                            return (int, fin_report[n],fin_report[m])

if __name__ == '__main__':

    report = open_file("input_day1.txt")
    #numbers = sum_search(report)
    #answer = numbers[0]*numbers[1]

    numbers = sum_search_three(report)
    answer = numbers[0]*numbers[1]*numbers[2]
    print(answer)

    end