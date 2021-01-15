
def load_file(filename, slope,line_length):
    infile = open(filename,'r')

    tree_num = 0
    position = 0
    max_position = line_length - 2
    incriment = slope

    for line in infile:
        #print(len(line))
        if line[position] =="#":
            tree_num += 1
        position+= incriment
        #check valid position
        if position > max_position:
            #if ouside range
            position -= max_position+1 #reset to start

    infile.close()
    return tree_num

def slope_two(filename,line_length):
    infile = open(filename,'r')

    tree_num = 0
    position = 1
    max_position = line_length-2
    incriment = 1
    down = 1
    init = 1

    for line in infile:
        if init == 1:
            #initial line
            init = 0
        elif down == 0:
            #do normal stuff
            if line[position] =="#":
                tree_num += 1
            position+= incriment
            #check valid position
            if position > max_position:
                #if ouside range
                position -= max_position+1 #reset to start
            down+= 1
            if down > 1:
                down = 0

        elif down == 1:
            #skip line
            down+= 1
            if down > 1:
                down = 0


    infile.close()
    return tree_num

if __name__ == "__main__":
    ans = []
    ans.append(load_file("input_day3.txt",1,32))
    ans.append(load_file("input_day3.txt",3,32))
    ans.append(load_file("input_day3.txt",5,32))
    ans.append(load_file("input_day3.txt",7,32))
    ans.append(slope_two("input_day3.txt",32))


    print(ans)
    print(ans[0]*ans[1]*ans[2]*ans[3]*ans[4])

    ans1 = []
    ans1.append(load_file("test_day3.txt",1,67))
    ans1.append(load_file("test_day3.txt",3,67))
    ans1.append(load_file("test_day3.txt",5,67))
    ans1.append(load_file("test_day3.txt",7,67))
    ans1.append(slope_two("test_day3.txt",67))


    print(ans1)
    print(ans1[0]*ans1[1]*ans1[2]*ans1[3]*ans1[4])