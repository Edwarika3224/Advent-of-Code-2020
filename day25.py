

filename = "input_day25.txt"
testfile = "test_day25.txt"
2084668
3704642
def parse(file):
    infile = open(file, 'r')

    for line in infile:
        break

    infile.close()
    pass

def part1(file):
    door_key = file[1]
    card_key = file[0]
    door_loop_size = get_loop_size(door_key)
    #card_loop_size = get_loop_size(card_key)
    return encrypt(door_loop_size,card_key)

def get_loop_size(key):
    '''
    With an initial subject number of 7, calculate the loop size used to create the key

    Input: Public Key
    return: The Loop Size
    '''
    temp = 1
    loop = 0
    while temp!=key:
        temp= (temp*7)%20201227
        loop+=1
    return loop

def encrypt(loop_size,subject_number):
    '''
    Encrypt the key for the given loop size
    return: Encryption key
    '''
    temp = 1
    for i in range(loop_size):
        temp *=subject_number
        temp = temp%20201227
    return temp

def part2(file):

    pass

if __name__ == "__main__":

    test_input = (5764801,17807724)
    input = (2084668,3704642)

    print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
