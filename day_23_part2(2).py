
'''
Part two of day 23 attempt 2
* Use a dictionary of all numbers that contains the number fter it in the list
* Makes lookup time alot easier
* Since only some parts of the list are edited, only a few values in the dictionary need to change
'''

import time

def initialize(dictionary = dict(), start = []):
    '''
    create the dictionary with the first 10 vales, and then append to 1,000,000
    '''
    #special values
    dictionary[start[-1]] = 10
    dictionary[1000000] = start[0]

    #initial order
    for i in range(0,len(start)-1):
        dictionary[start[i]] = start[i+1]

    #remaining values
    for i in range(10,1000000):
        dictionary[i] = i+1

def part2(file):
    cup_order = dict()
    initialize(cup_order,list(map(int,file))) #create the dictionary

    current_cup = int(file[0])
    for i in range(100000):
        current_cup = move(cup_order,current_cup)

    return final(cup_order)

def move(cup_order,current):
    '''
    Perform the set of moves necessary in the game once
    Updates the Dictionary as needed

    Input: cup_order - a dictionary of the cups and the value after them
           current - the current cup in around which to move

    Return: a new current cup after the the set of moves is performed
    '''

    #Step 1 : Get the three removed vales after the current value
    val1 = cup_order[current]
    val2 = cup_order[val1]
    val3 = cup_order[val2]
    #Step 1.1: connect the list where the values are missing
    connector =  cup_order[val3]
    cup_order[current] = connector

    #Step 2: Select a destination cup
    dest = destination(current,[val1,val2,val3])
    #Step 3 Place the three cups down after the destination and fix the order of the list
    gap_end = cup_order[dest]
    cup_order[dest] = val1
    cup_order[val3] = gap_end

    #Step 4: Select the new current cup; one which was clockwise from the previous
    return connector


def destination(current,removed):
    '''
    Select a destination cups based on the current cup
    
    Input: current - The Current cup used in the move
           removed - A list of the three removed cups 

    return: The value of the destination cup
    '''
    dest = current-1
    while(True):
        if dest in removed:
            dest-=1
        elif dest <= 0:
            dest = 1000000
        else:
            #destination is in list
            return dest
    raise AssertionError

def final(cup_order):
    '''
    Use the cup order to determien the multiple of the two values imediatly after 1

    Input: cup_order - A dictionary of all values that tells what comes before and after

    Return: The multiple of the two values after 1
    '''
    val1 = cup_order[1]
    val2 = cup_order[val1]
    print("The two determiend values are: ", val1,val2)
    return val1*val2

if __name__ == "__main__":
    test_input = "389125467"
    input = "463528179"

    start = time.time()
    print(part2(test_input))
    end = time.time()
    print("Time for Test run: ", end-start)


    start = time.time()
    print(part2(input))
    end = time.time()
    print("Time for run: ", end-start)
