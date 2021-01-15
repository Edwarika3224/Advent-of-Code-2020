

filename = "input_day12.txt"
testfile = "test_day12.txt"

def parse(file):
    return open(file, 'r').read().splitlines()

def part1(file):

    direction = 'E'
    position = [0,0]

    for entry in file:
        if entry[0] == 'E':
            position[0]+=int(entry[1:])
        elif entry[0] == 'W':
            position[0]-=int(entry[1:])
        elif entry[0] == 'N':
            position[1]+=int(entry[1:])
        elif entry[0] == 'S':
            position[1]-=int(entry[1:])

        elif entry[0] == 'F':
            if direction== 'E':
                position[0]+=int(entry[1:])
            elif direction == 'W':
                position[0]-=int(entry[1:])
            elif direction == 'N':
                position[1]+=int(entry[1:])
            elif direction == 'S':
                position[1]-=int(entry[1:])
        else:
            direction = rotate(direction,entry)
    return abs(position[0])+abs(position[1])

def rotate(dir,entry):
    map90R = {'E':'S', 'S':'W', 'W':'N', 'N':'E' }
    map180 = {'E':'W', 'S':'N', 'W':'E', 'N':'S' }
    map90L = {'E':'N', 'S':'E', 'W':'S', 'N':'W' }

    if entry[0] == 'R':
        if entry[1:] == '90':
            return map90R[dir]
        elif entry[1:] == '180':
            return map180[dir]
        elif entry[1:] == '270':
            return map90L[dir]
        else:
            raise AttributeError
    else:
        if entry[1:] == '90':
            return map90L[dir]
        elif entry[1:] == '180':
            return map180[dir]
        elif entry[1:] == '270':
            return map90R[dir]
        else:
            raise AttributeError

def part2(file):

    waypoint = [10,1]
    position = [0,0]

    for entry in file:
        if entry[0] == 'E':
            waypoint[0]+=int(entry[1:])
        elif entry[0] == 'W':
            waypoint[0]-=int(entry[1:])
        elif entry[0] == 'N':
            waypoint[1]+=int(entry[1:])
        elif entry[0] == 'S':
            waypoint[1]-=int(entry[1:])

        elif entry[0] == 'F':
            position[0]+=waypoint[0]*int(entry[1:])
            position[1]+=waypoint[1]*int(entry[1:])
        else:
             waypoint = rotate_waypoint(waypoint,entry)
    return abs(position[0])+abs(position[1])

def rotate_waypoint(waypoint,entry):

    if entry[0] == 'R':
        if entry[1:] == '90':
            return R90(waypoint,entry)
        elif entry[1:] == '180':
            return R180(waypoint,entry)
        elif entry[1:] == '270':
            return L90(waypoint,entry)
        else:
            raise AttributeError
    else:
        if entry[1:] == '90':
            return L90(waypoint,entry)
        elif entry[1:] == '180':
            return R180(waypoint,entry)
        elif entry[1:] == '270':
            return R90(waypoint,entry)
        else:
            raise AttributeError

def R90(waypoint,entry):
    new_waypoint = [0,0]
    new_waypoint[0] = waypoint[1]
    new_waypoint[1] = 0-waypoint[0]
    return new_waypoint

def R180(waypoint,entry):
    new_waypoint = [0,0]
    new_waypoint[0] = 0-waypoint[0]
    new_waypoint[1] = 0-waypoint[1]
    return new_waypoint

def L90(waypoint,entry):
    new_waypoint = [0,0]
    new_waypoint[0] = 0-waypoint[1]
    new_waypoint[1] = waypoint[0]
    return new_waypoint

if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    print(part1(test_input))
    print(part2(test_input))

    print(part1(input))
    print(part2(input))
