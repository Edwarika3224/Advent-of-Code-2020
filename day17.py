from day11 import Seats,Alt_Seats
import time


filename = "input_day17.txt"
testfile = "test_day17.txt"

def parse(file):
    return open(file, 'r').read().splitlines()

class Cubespace(object):
    '''
    A space of cubes either active or inactive
    list of all cubes within range of starting zone stored in self.cubes
    self.cubes also stores the state of each cube

    Note: cubespace is left handed
    '''
    def __init__(self,cubelist):
        '''
        Cubelist takes a file of cubes states with any x and y length but only one z length
        '''
        self.xrange = range(-6,len(cubelist)+6)
        self.yrange = range(-6,len(cubelist[0])+6)
        self.zrange = range(-6,7)
        self.cubes = {}
        #Initialize all cubes
        for z in self.zrange:
            for x in self.xrange:
                for y in self.yrange:
                    self.cubes[x,y,z] = False
        for i in range(len(cubelist)):
            for n in range(len(cubelist[0])):
                if cubelist[i][n] == '#':
                    self.cubes[(i,n,0)] = True
    def get_active(self):
        '''
        return the number of active cubes in the Cubespace
        '''
        active = 0
        for state in self.cubes.values():
            if state:
                active+=1
        return active
    def cycle(self):
        '''
        puts all cubes through one cycle of change
        '''
        change = [] # list of cubes that need to be changed
        for cube in self.cubes:
            if self.check(cube):
                change.append(cube)
        
        #update
        for cube in change:
            self.cubes[cube] = not self.cubes[cube]

        return
    def check(self, location = (0,0,0)):
        '''
        check if the state of the cube should change
        '''
        x = location[0]
        y = location[1]
        z = location[2]
        #check for special cubes
        #special cubes are all cubes on the side planes of the cubespace
        #if any([x == -6,
        #       y == -6,
        #       z == -6,
        #       x == self.xrange[-1],
        #       y == self.yrange[-1],
        #       z == self.zrange[-1]]):
        #    return self.check_special(x,y,z)
        if self.cubes[location]:
            #cube is active
            return self.check_active(x,y,z)
        else:
            #cube is inactive
            return self.check_inactive(x,y,z)
        raise AssertionError
    def check_special(self,x,y,z):
        '''
        check cubes at special locations
        #different special locaitons are: 
            1. eight corner points
            2. twelve edge lines
            3. six face planes
        '''
        #corner check
        if z == -6: 
            #back plane
            if x == -6: 
                #left side
                if y == -6: 
                    # top side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[14,16,17,22,23,25,26])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[14,16,17,22,23,25,26])
                else: 
                    #bottom side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[11,12,14,19,20,22,23])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[11,12,14,19,20,22,23])
            else: 
                #right side
                if y == -6:
                    #top side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[13,15,16,21,22,24,25])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[13,15,16,21,22,24,25])
                else:
                    #bottom side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[10,11,13,18,19,21,22])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[10,11,13,18,19,21,22])
        else:
            #front plane
            if x == -6:
                #left side
                if y == -6:
                    #top side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[5,6,8,9,14,16,17])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[5,6,8,9,14,16,17])
                else:
                    #bottom side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[2,3,5,6,11,12,14])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[2,3,5,6,11,12,14])
            else:
                #right side
                if y == -6:
                    #top side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[4,5,7,8,13,15,16])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[4,5,7,8,13,15,16])
                else:
                    #bottom side
                    if self.cubes[(x,y,z)]:
                        #active
                        return self.check_active(x,y,z,[1,2,4,5,10,11,13])
                    else:
                        #inactive
                        return self.check_inactive(x,y,z,[1,2,4,5,10,11,13])


        #edge check
        if z == -6:
            #back plane
            if x == -6:
                #left edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[11,12,14,16,17,29,20,22,23,25,26])
                else:
                    return self.check_inactive(x,y,z,[11,12,14,16,17,29,20,22,23,25,26])
            elif x == self.xrange[-1]:
                #right edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[10,11,13,15,16,18,19,21,22,24,25])
                else:
                    return self.check_inactive(x,y,z,[10,11,13,15,16,18,19,21,22,24,25])
            elif y == -6:
                #top edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[13,14,15,16,17,21,22,23,24,25,26])
                else:
                    return self.check_inactive(x,y,z,[13,14,15,16,17,21,22,23,24,25,26])
            else:
                #bottom edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[10,11,12,13,14,18,19,20,21,22,23])
                else:
                    return self.check_inactive(x,y,z,[10,11,12,13,14,18,19,20,21,22,23])
        elif z == 6:
            #front plane
            if x == -6:
                #left edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[2,3,5,6,8,9,11,12,14])
                else:
                    return self.check_inactive(x,y,z,[2,3,5,6,8,9,11,12,14])
            elif x == self.xrange[-1]:
                #right edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[1,2,4,5,7,8,10,11,13])
                else:
                    return self.check_inactive(x,y,z,[1,2,4,5,7,8,10,11,13])
            elif y == -6:
                #top edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[4,5,6,7,8,9,13,14,15,16,17])
                else:
                    return self.check_inactive(x,y,z,[4,5,6,7,8,9,13,14,15,16,17])
            else:
                #bottom edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[1,2,3,4,5,6,10,11,12,13,14])
                else:
                    return self.check_inactive(x,y,z,[1,2,3,4,5,6,10,11,12,13,14])
        elif y == -6:
            # top plane
            if x == -6:
                #left edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[5,6,8,9,14,16,17,22,23,25,26])
                else:
                    return self.check_inactive(x,y,z,[5,6,8,9,14,16,17,22,23,25,26])
            else:
                #right edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[4,5,7,8,13,15,16,21,22,24,25])
                else:
                    return self.check_inactive(x,y,z,[4,5,7,8,13,15,16,21,22,24,25])
        else:
            #bottom plane
            if x == -6:
                #left edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[2,3,5,6,11,12,14,19,20,22,23])
                else:
                    return self.check_inactive(x,y,z,[2,3,5,6,11,12,14,19,20,22,23])
            else:
                #right edge
                if self.cubes[(x,y,z)]:
                    #active
                    return self.check_active(x,y,z,[1,2,4,5,10,11,13,18,19,21,22])
                else:
                    return self.check_inactive(x,y,z,[1,2,4,5,10,11,13,18,19,21,22])

        #plane check
        if z == -6:
            #back plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,list(range(10,27)))
            else:
                #inactive
                return self.check_inactive(x,y,z,list(range(10,27)))
        elif z == 6:
            #front plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,list(range(1,18)))
            else:
                #inactive
                return self.check_inactive(x,y,z,list(range(1,18)))
        elif y == -6:
            #top plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,[4,5,6,7,8,9,13,14,15,16,17,21,22,23,24,25,26])
            else:
                #inactive
                return self.check_inactive(x,y,z,[4,5,6,7,8,9,13,14,15,16,17,21,22,23,24,25,26])
        elif y == self.yrange[-1]:
            #bottom plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,[1,2,3,4,5,6,10,11,12,13,14,18,19,20,21,22,23])
            else:
                #inactive
                return self.check_inactive(x,y,z,[1,2,3,4,5,6,10,11,12,13,14,18,19,20,21,22,23])
        elif x == -6:
            #left plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,[2,3,5,6,8,9,11,12,14,16,17,19,20,22,23,25,26])
            else:
                #inactive
                return self.check_inactive(x,y,z,[2,3,5,6,8,9,11,12,14,16,17,19,20,22,23,25,26])
        else:
            #right plane
            if self.cubes[(x,y,z)]:
                #active
                return self.check_active(x,y,z,[1,2,4,5,7,8,10,11,13,15,16,18,19,21,22,24,25])
            else:
                #inactive
                return self.check_inactive(x,y,z,[1,2,4,5,7,8,10,11,13,15,16,18,19,21,22,24,25])
        raise AssertionError("Could not determine special location")
    def check_active(self,x,y,z,array = list(range(1,27))):
        '''
        Check active cubes if they need to be chenged
        default check all locations around the cube
        for specific locaitons:
            z=-1:   1 2 3
                    4 5 6
                    7 8 9

            z=+0:   10 11 12
                    13    14
                    15 16 17

            z=+1:   18 19 20
                    21 22 23
                    24 25 26
        '''
        c ={1:  (x-1,y-1,z-1),
            2:  (x  ,y-1,z-1),
            3:  (x+1,y-1,z-1),
            4:  (x-1,y  ,z-1),
            5:  (x  ,y  ,z-1),
            6:  (x+1,y  ,z-1),
            7:  (x-1,y+1,z-1),
            8:  (x  ,y+1,z-1),
            9:  (x+1,y+1,z-1),

            10: (x-1,y-1,z  ),
            11: (x  ,y-1,z  ),
            12: (x+1,y-1,z  ), 
            13: (x-1,y  ,z  ),
            14: (x+1,y  ,z  ),
            15: (x-1,y+1,z  ),
            16: (x  ,y+1,z  ),
            17: (x+1,y+1,z  ),

            18: (x-1,y-1,z+1),
            19: (x  ,y-1,z+1),
            20: (x+1,y-1,z+1),
            21: (x-1,y  ,z+1),
            22: (x  ,y  ,z+1),
            23: (x+1,y  ,z+1),
            24: (x-1,y+1,z+1),
            25: (x  ,y+1,z+1),
            26: (x+1,y+1,z+1),} # Variable used to map number to location
        num = 0
        for spot in array:
            try:
                if self.cubes[c[spot]]:
                    num+=1
            except:
                continue

        if num == 2 or num == 3:
            return False
        return True
    def check_inactive(self,x,y,z,array = list(range(1,27))):
        '''
        Check passive cubes if they need to be chenged
        default check all locations around the cube
        for specific locaitons:
            z=-1:   1 2 3
                    4 5 6
                    7 8 9

            z=+0:   10 11 12
                    13    14
                    15 16 17

            z=+1:   18 19 20
                    21 22 23
                    24 25 26
        '''
        c ={1:  (x-1,y-1,z-1),
            2:  (x  ,y-1,z-1),
            3:  (x+1,y-1,z-1),
            4:  (x-1,y  ,z-1),
            5:  (x  ,y  ,z-1),
            6:  (x+1,y  ,z-1),
            7:  (x-1,y+1,z-1),
            8:  (x  ,y+1,z-1),
            9:  (x+1,y+1,z-1),

            10: (x-1,y-1,z  ),
            11: (x  ,y-1,z  ),
            12: (x+1,y-1,z  ), 
            13: (x-1,y  ,z  ),
            14: (x+1,y  ,z  ),
            15: (x-1,y+1,z  ),
            16: (x  ,y+1,z  ),
            17: (x+1,y+1,z  ),

            18: (x-1,y-1,z+1),
            19: (x  ,y-1,z+1),
            20: (x+1,y-1,z+1),
            21: (x-1,y  ,z+1),
            22: (x  ,y  ,z+1),
            23: (x+1,y  ,z+1),
            24: (x-1,y+1,z+1),
            25: (x  ,y+1,z+1),
            26: (x+1,y+1,z+1),} # Variable used to map number to location
        num = 0
        for spot in array:
            try:
                if self.cubes[c[spot]]:
                    num+=1
            except:
                continue

        if num == 3:
            return True
        return False

class Hypercube(Cubespace):
    def __init__(self,cubelist):
        self.xrange = range(-6,len(cubelist)+6)
        self.yrange = range(-6,len(cubelist[0])+6)
        self.zrange = range(-6,7)
        self.wrange = range(-6,7)
        self.cubes = {}
        #Initialize all cubes
        for w in self.wrange:
            for z in self.zrange:
                for x in self.xrange:
                    for y in self.yrange:
                        self.cubes[x,y,z,w] = False
        for i in range(len(cubelist)):
            for n in range(len(cubelist[0])):
                if cubelist[i][n] == '#':
                    self.cubes[(i,n,0,0)] = True
    def check(self, location = (0,0,0,0)):
        '''
        check if the state of the cube should change
        '''
        x = location[0]
        y = location[1]
        z = location[2]
        w = location[3]
        #check for special cubes
        #special cubes are all cubes on the side planes of the cubespace
        #if any([x == -6,
        #       y == -6,
        #       z == -6,
        #       x == self.xrange[-1],
        #       y == self.yrange[-1],
        #       z == self.zrange[-1]]):
        #    return self.check_special(x,y,z)
        if self.cubes[location]:
            #cube is active
            return self.check_change(x,y,z,w,True)
        else:
            #cube is inactive
            return self.check_change(x,y,z,w,False)
        raise AssertionError
    def check_change(self,x,y,z,w,state):
        num = 0
        for dw in range(-1,2):
            for dz in range(-1,2):
                for dy in range (-1,2):
                    for dx in range(-1,2):
                        try:
                            if self.cubes[(x+dx,y+dy,z+dz,w+dw)]:
                                num+=1
                        except:
                            continue

        if state:
            if num ==3 or num ==4:
                return False
            else:
                return True
        else:
            if num == 3:
                return True
            else:
                return False
        raise AttributeError


def part1(file):

    space = Cubespace(file)
    for i in range(6):
        space.cycle()
    return space.get_active()


def part2(file):

    space = Hypercube(file)
    for i in range(6):
        space.cycle()
    return space.get_active()

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    start = time.time()
    print(part2(test_input))
    end = time.time()
    print("test time: ", end-start)

    #print(part1(input))
    start = time.time()
    print(part2(input))
    end = time.time()
    print("run time: ", end-start)
