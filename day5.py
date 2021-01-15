from advent_of_code import openfile

filename = "input_day5.txt"

def part1(file):
    passes = []
    largest = 0
    for line in file:        
        passes.append(get_seat(line.strip('\n')))
    for entry in passes:
        temp = entry[0]*8 + entry[1]
        if temp > largest:
            largest = temp
    return largest


def part2(file):
    passes = []
    pass_id = []
    for line in file:        
        passes.append(get_seat(line.strip('\n')))
    for entry in passes:
        pass_id.append(entry[0]*8 + entry[1])
    
    pass_id.sort()
    for i in range(len(pass_id)):
        if pass_id[i]+1 != pass_id[i+1]:
            if pass_id[i]+2 == pass_id[i+1]:
                return pass_id[i]+1
    raise ArithmeticError


def get_seat(code):
    row_upper = 127
    row_lower = 0
    row = 0

    seat_upper = 7
    seat_lower = 0
    seat = 0
    
    for char in code[0:7]:
        if char == 'F':
            row_upper-= int((row_upper-row_lower)/2)+1
        else:
            row_lower+= int(1+((row_upper-row_lower)/2))
    if row_lower == row_upper:
        row = row_lower
    else:
        raise ArithmeticError

    for char in code[-3::]:
        if char == 'L':
            seat_upper-= int((seat_upper-seat_lower)/2)+1
        else:
            seat_lower+= int(1+((seat_upper-seat_lower)/2))
    if seat_lower == seat_upper:
        seat = seat_lower
    else:
        raise ArithmeticError

    return (row,seat)

if __name__ == "__main__":

    #print(part1(openfile(filename)))
    print(part2(openfile(filename)))