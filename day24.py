

filename = "input_day24.txt"
testfile = "test_day24.txt"

def parse(file):
    infile = open(file, 'r').read().splitlines()
    return infile

def part1(file):
    black = set()

    for line in file:
        flip = get_tile(decode_inst(line))
        if flip in black:
            black.remove(flip)
        else:
            black.add(flip)
    return len(black)


def decode_inst(line):
    inst = []
    North = False
    South = False
    for char in line:
        if North:
            if char == 'e':
                inst.append('NE')
            elif char == 'w':
                inst.append('NW')
            North = False
        elif South:
            if char == 'e':
                inst.append('SE')
            elif char == 'w':
                inst.append('SW')
            South = False
            North = False
        elif char == 'e':
            inst.append('E')
        elif char == 'w':
            inst.append('W')
        elif char == 'n':
            North = True
        elif char == 's':
            South = True
    return inst

def get_tile(inst):
    position = [0,0]
    for instruction in inst:
        if instruction == "E":
            position[0]+=1
        if instruction == "W":
            position[0]-=1
        if instruction == "NE":
            if position[1]%2:
                #is even
                position[1]+=1
            else:
                position[1]+=1
                position[0]+=1
        if instruction == "NW":
            if position[1]%2:
                #is even
                position[1]+=1
                position[0]-=1
            else:
                position[1]+=1
        if instruction == "SE":
            if position[1]%2:
                #is even
                position[1]-=1
            else:
                position[1]-=1
                position[0]+=1
        if instruction == "SW":
            if position[1]%2:
                #is even
                position[0]-=1
                position[1]-=1
            else:
                position[1]-=1
    return tuple(position)

def part2(file):

    grid = floor(file)
    grid.update_v2(100,file)
    return grid.get_black()

class floor(object):
    def __init__(self,instructions):
        self.daily_flip = []
        for line in instructions:
            temp = get_tile(decode_inst(line))
            if temp not in self.daily_flip:
                self.daily_flip.append(temp)
        self.flipped = set()

    def get_black(self):
        return len(self.flipped)
    def update(self,days):
        while(days): #run for x amount of days
            flip = set() #set of tiles to be flipped
            for entry in self.daily_flip:
                flip.add(entry) #add the tiles that flip every day

            self.determine(flip) #determine all new tiles

            #now update every tile that needs to be flipped
            for entry in flip:
                try:
                    self.flipped.remove(entry)
                except KeyError:
                    self.flipped.add(entry)

            days-=1
    def update_v2(self,days,inst):
        self.initialize(inst)
        while(days): #run for x amount of days
            flip = set() #set of tiles to be flipped

            self.determine(flip) #determine all new tiles

            #now update every tile that needs to be flipped
            for entry in flip:
                try:
                    self.flipped.remove(entry)
                except KeyError:
                    self.flipped.add(entry)

            days-=1
    def initialize(self,inst):
        for line in inst:
            flip =  get_tile(decode_inst(line))
            try:
                self.flipped.remove(flip)
            except KeyError:
                self.flipped.add(flip)
    def determine(self,flip):
        also = set()
        for entry in self.flipped:
            temp = self.adj(entry)
            if entry in flip:
                pass
            else:             
                if self.check(temp,True):
                    flip.add(entry)
            for new in temp:
                also.add(new)

        for entry in also:
            temp = self.adj(entry)
            state = entry in self.flipped
            if entry in flip:
                continue
            else:             
                if self.check(temp,state):
                    flip.add(entry)
    def adj(self,tile):
        adj = []
        if tile[1]%2:
            adj.extend([
                (tile[0]+1,tile[1]),
                (tile[0]-1,tile[1]),
                (tile[0]  ,tile[1]+1),
                (tile[0]  ,tile[1]-1),
                (tile[0]-1,tile[1]+1),
                (tile[0]-1,tile[1]-1)])
        else:
            adj.extend([
                (tile[0]+1,tile[1]),
                (tile[0]-1,tile[1]),
                (tile[0]  ,tile[1]+1),
                (tile[0]  ,tile[1]-1),
                (tile[0]+1,tile[1]+1),
                (tile[0]+1,tile[1]-1)])
        return adj
    def check(self,adj = [], state = bool):
        num = 0
        for tile in adj:
            if tile in self.flipped:
                num+=1
        if state:
            if num == 0 or num>2:
                return True
        else:
            if num ==2:
                return True
        return False

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
