import time

filename = "input_day10.txt"
testfile = "test_day10.txt"

def parse(file):
    infile = open(file, 'r')

    ans = []
    lines = infile.read().splitlines()
    for line in lines:
        ans.append(int(line))

    infile.close()
    ans.append(0)
    ans.sort()
    ans.append(ans[-1]+3)
    return ans

def part1(file):

    volt = 0
    ones = 0
    threes = 0
    for entry in file:
        if entry-1 == volt:
            ones+=1
        elif entry-3 == volt:
            threes+=1
        volt = entry

    return ones*threes


def part2_recursion(file):
    valid = [0,3]
    mem = dict()
    get_chain(0,file[1::],valid,mem)
    return valid[0]

def part2_calculation(file):

    valid = 1
    for i in range(len(file)):
        split = get_split(file,i)
        valid = valid*split
    return valid

def part2_calc_revised(array):
    split = {}
    valid=1
    for i in range(len(array)):
        split[i+1] = get_split(array,i)

    i=0
    while i<len(array):
        if split[i] == 3:
            valid = valid*4
            if split[i+1] <3:
                i+=2
        elif split[i] == 2:
            valid = valid*2
            if split[i+1] <=2:
                i+=1
        i+=1
    return valid
        

def part2_pub(file):
    '''
    based off of calculating how many locations the location could have come from
    i.e how many spots could have jumped to this locaiton
    '''
    jolts = file[1::]
    dp = {0: 1}

    for jolt in jolts:
        dp[jolt] = 0
        if jolt - 1 in dp:
            dp[jolt] += dp[jolt - 1]
        if jolt - 2 in dp:
            dp[jolt] += dp[jolt - 2]
        if jolt - 3 in dp:
            dp[jolt] += dp[jolt - 3]

    return dp[jolts[-1]]
            
def get_split(file,i):
    '''
    returns the number of times the file splits at the givin location
    i.e how many spots it can jump to
    '''
    try:
        if file[i+3]-file[i]<=3:
            return 3
        if file[i+2]-file[i]<=3:
            return 2
        else:
            return 1
    except:
        try:
            if file[i+2]-file[i]<=3:
                return 2
            else:
                return 1
        except:
            return 1


def get_chain(volt, file, valid,mem):

    if volt in mem:
        valid[0]+= mem[volt]
        return
    if len(file) == 1:
        valid[0]+=1
        mem[volt] = 1
        return
    curent = valid[0]
    try:
        if file[2]-volt<=3:
            for entry in range(3):
                get_chain(file[entry],file[entry+1::],valid,mem)
        elif file[1]-volt<=3:
            for entry in range(2):
                get_chain(file[entry],file[entry+1::],valid,mem)
        else:
            get_chain(file[0],file[1::],valid,mem)
        mem[volt] = valid[0]-curent
        return
    except:
        if file[1]-volt<=3:
            for entry in range(2):
                get_chain(file[entry],file[entry+1::],valid,mem)
        else:
            get_chain(file[0],file[1::],valid,mem)
        mem[volt] = valid[0]-curent
        return
    raise AssertionError
    

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part2_pub(test_input))
    #print(part2_calc_revised(test_input))
    print(part2_recursion(test_input))


    
    #print(part1(test_input))
    #print(part2(test_input))

    #print(part1(input))

    start = time.time()
    print(part2_pub(input))
    end = time.time()
    print(end - start)

    start = time.time()
    print(part2_recursion(input))
    end = time.time()
    print(end - start)
