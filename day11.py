import time

filename = "input_day11.txt"
testfile = "test_day11.txt"

def parse(file):
    infile = open(file, 'r')

    seats = infile.read().splitlines()

    infile.close()
    return seats

def part1(file):

    area = Seats(file)
    while(area.update()):
        1
    return area.num_taken()

def part2(file):
    area = Alt_Seats(file)
    while(area.update()):
        1
    return area.num_taken()


class Seats(object):
    def __init__(self,seatlist):
        self.rows = len(seatlist)
        self.colemns = len(seatlist[0])
        self.seats = {}
        for i in range(len(seatlist)):
            for n in range(len(seatlist[0])):
                if seatlist[i][n] == 'L':
                    self.seats[(i,n)] = True
                else:
                    self.seats[(i,n)] = False
        self.occupied = {}
        for i in range(len(seatlist)):
            for n in range(len(seatlist[0])):
                self.occupied[i,n] = False

    def check_seats(self, seat, occupied, seats = {1,2,3,4,6,7,8,9}):
        '''
        input: seats - a set of seats to check from 1-9
               seat positions:  1 2 3
                                4 5 6
                                7 8 9
               #seat 5 should never be checked
                            
               seat - the seat we are checking around; seat 5
               occupied - if the seat is occupied or not
    
        output: True if seat 5 should be changed or not
        '''
        s ={1: (seat[0]-1, seat[1]-1),
            2: (seat[0]-1, seat[1]),
            3: (seat[0]-1, seat[1]+1),
            4: (seat[0], seat[1]-1),
            6: (seat[0], seat[1]+1),
            7: (seat[0]+1, seat[1]-1),
            8: (seat[0]+1, seat[1]),
            9: (seat[0]+1, seat[1]+1)}
        if occupied:
            #if seat number 5 is occupied check the seats given and see if the seat should be changed
            taken = 0
            for entry in seats:
                if self.occupied[s[entry]]:
                    taken+=1
            if taken > 3:
                return True
            return False
        else:
            #if seat number 5 is unocccupied check if there are no seats adjacent whiche are occupied
            for entry in seats:
                if self.occupied[s[entry]]:
                    return False
            return True

    def num_taken(self):
        taken = 0
        for entry in self.occupied.values():
            if entry:
                taken+=1
        return taken

    def check_special(self,i,n):
        '''
        special seats
        '''
        if any([i ==0 and n == 0,
                i ==0 and n == self.colemns-1,
                i == self.rows-1 and n ==0,
                i == self.rows-1 and n == self.colemns-1]):
            #corners
            if self.occupied[(i,n)]:
                #occiupied
                return False 
            else:
                return True
        elif i == 0:
            #top row
            if self.occupied[(i,n)]:
                #taken
                return self.check_seats((i,n),True,{4,6,7,8,9})
            else:
                return self.check_seats((i,n),False,{4,6,7,8,9})
        elif i == self.rows-1:
            #bottom row
            if self.occupied[(i,n)]:
                #taken
                return self.check_seats((i,n),True,{1,2,3,4,6})
            else:
                return self.check_seats((i,n),False,{1,2,3,4,6})
        elif n == 0:
            #left side
            if self.occupied[(i,n)]:
                #taken
                return self.check_seats((i,n),True,{2,3,6,8,9})
            else:
                return self.check_seats((i,n),False,{2,3,6,8,9})
        elif n == self.colemns-1:
            #right side
            if self.occupied[(i,n)]:
                #taken
                return self.check_seats((i,n),True,{1,2,4,7,8})
            else:
                return self.check_seats((i,n),False,{1,2,4,7,8})

        raise AssertionError

    def check(self,i,n):
        '''
        check if the position should be updated
        '''
        #check if seat exists
        if not self.seats[(i,n)]:
            #not a seat
            return False

        #check for special seats
        if any([i == 0,
                n == 0,
                i == self.rows-1,
                n == self.colemns-1]):
            return self.check_special(i,n)

        elif self.occupied[(i,n)]:
            #seat is occupied check if should be unoccupied
            return self.check_seats((i,n),True) 
        else:
            #seat is unoccupied
            return self.check_seats((i,n),False)

    def update(self):
        '''
        update all seast
        check if they need to update then update the ones that need to

        return: if at least one seat changed or not
        '''
        updated = dict()
        changed = 0
        for i in range(self.rows):
            for n in range(self.colemns):
                updated[(i,n)] = self.check(i,n)
        for i in range(self.rows):
            for n in range(self.colemns):
                if updated[(i,n)]:
                    changed+=1
                    self.commit(i,n)
        if changed == 0:
            return False
        return True

    def commit(self,i,n):
        if not self.seats[(i,n)]:
            raise AssertionError
        if self.occupied[(i,n)]:
            self.occupied[(i,n)] = False
        else:
            self.occupied[(i,n)] = True


class Alt_Seats(Seats):
    def check(self,i,n):
        '''
        check if the position should be updated
        '''
        #check if seat exists
        if not self.seats[(i,n)]:
            #not a seat
            return False

        # if it is a seat then check
        seats = self.get_seats(i,n)
        if self.occupied[(i,n)]:
            taken = 0
            for seat in seats:
                if self.occupied[seat]:
                    taken+=1
            if taken > 4:
                return True
            return False
        else:
            for seat in seats:
                if self.occupied[seat]:
                    return False
            return True

        raise AssertionError
    def get_seats(self,i,n):
        '''
        get the location of the first seat that is seen from the given location

        if there are no seen seats in that direction, returns no seat.
        '''
        seen = []
        for direction in range(8):
            #for the 8 directions
            if direction == 0:
                #check left
                try:
                    k = 1
                    while(1):
                        if self.seats[i,n-k]:
                            seen.append((i,n-k))
                            break
                        k+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 1:
                #check upperleft
                try:
                    k = 1
                    j = 1
                    while(1):
                        if self.seats[i-j,n-k]:
                            seen.append((i-j,n-k))
                            break
                        k+=1
                        j+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 2:
                #check above
                try:
                    k = 1
                    while(1):
                        if self.seats[i-k,n]:
                            seen.append((i-k,n))
                            break
                        k+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 3:
                #check upperright
                try:
                    k = 1
                    j=1
                    while(1):
                        if self.seats[i-j,n+k]:
                            seen.append((i-j,n+k))
                            break
                        k+=1
                        j+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 4:
                #check right side
                try:
                    k = 1
                    while(1):
                        if self.seats[i,n+k]:
                            seen.append((i,n+k))
                            break
                        k+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 5:
                #check bottom right
                try:
                    k = 1
                    j = 1
                    while(1):
                        if self.seats[i+j,n+k]:
                            seen.append((i+j,n+k))
                            break
                        k+=1
                        j+=1
                except:
                    #no seats in that direction
                    0
            elif direction == 6:
                #check below
                try:
                    k = 1
                    while(1):
                        if self.seats[i+k,n]:
                            seen.append((i+k,n))
                            break
                        k+=1
                except:
                    #no seats in that direction
                    0
            else:
                #check bottom left
                try:
                    k = 1
                    j = 1
                    while(1):
                        if self.seats[i+j,n-k]:
                            seen.append((i+j,n-k))
                            break
                        k+=1
                        j+=1
                except:
                    #no seats in that direction
                    0
        return seen

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    start = time.time()
    print(part1(test_input))
    end = time.time()
    print("Part 1 test time taken = ",end-start)

    start = time.time()
    print(part2(test_input))
    end = time.time()
    print("Part 2 test time taken = ",end-start)

    start = time.time()
    print(part1(input))
    end = time.time()
    print("Part 1 time taken = ",end-start)

    start = time.time()
    print(part2(input))
    end = time.time()
    print("Part 2 time taken = ",end-start)