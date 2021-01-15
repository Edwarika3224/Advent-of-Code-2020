

filename = "input_day22.txt"
testfile = "test_day22.txt"

def parse(file):
    infile = open(file, 'r').read().split('\n\n')
    player1 = list(map(int, infile[0].split('\n')[1:]))
    player2 = list(map(int, infile[1].split('\n')[1:]))
    return player1,player2

def part1(file):

    player1 = file[0]
    player2 = file[1]
    winner = game(player1,player2)
    return get_score(winner)

def game(p1 = [],p2 = []):
    if p1 == []:
        return p2
    if p2 == []:
        return p1

    cards = []
    cards.append(p1.pop(0))
    cards.append(p2.pop(0))
    if cards[0] > cards[1]:
        p1.extend(cards)
    else:
        p2.append(cards[1])
        p2.append(cards[0])

    return game(p1,p2)

def get_score(win = []):
    length = len(win)
    score = 0
    for i in range(length):
        score+=(i+1)*win[-1-i]
    return score

def part2(file):

    player1 = file[0]
    player2 = file[1]
    winner = recursive_three(player1,player2)
    if winner == 1:
        return get_score(player1)
    else:
        return get_score(player2)
    #return get_score(winner[1])

def recursive(p1 = (), p2 = (), p1_decks = set(),p2_decks = set()):
    '''
    recursive game
    returns: 1 on player1 win
             2 on player2 win
    '''
    if p1 == ():
        return 2,p2e
    if p2 == ():
        return 1,p2

    if p1 in p1_decks or p2 in p2_decks:
        return 1,p1
    p1_decks.add(p1)
    p2_decks.add(p2)
    
    cards = []
    cards.append(p1[0])
    cards.append(p2[0])
    if not (cards[0] >= len(p1) or cards[1] >= len(p2)):
        #new recursive game to determine winner
        winner = recursive(tuple(p1[1:cards[0]]),tuple(p2[1:cards[1]]), set(), set())
        #if cards[1] > cards[0]:
        #    cards = [cards[1],cards[0]]
        if winner[0] == 1:
            p1 = tuple(p1[1:]+(cards[0],cards[1]))
            p2 = p2[1:]
        else:
            p1 = p1[1:]
            p2 = tuple(p2[1:]+(cards[1],cards[0]))
    else:
        #normal game
        if cards[0] > cards[1]:
            p1 = tuple(p1[1:]+(cards[0],cards[1]))
            p2 = p2[1:]
        else:
            p1 = p1[1:]
            p2 = tuple(p2[1:]+(cards[1],cards[0]))
    return recursive(p1,p2,p1_decks, p2_decks)

def recursive_lists(p1 = [], p2 = [], p1_decks = [],p2_decks = []):
    '''
    recursive game
    returns: 1 on player1 win
             2 on player2 win
    '''
    if p1 == []:
        return 2
    if p2 == []:
        return 1

    if p1 in p1_decks or p2 in p2_decks:
        return 1
    p1_decks.append(p1[:])
    p2_decks.append(p2[:])
    
    cards = []
    cards.append(p1.pop(0))
    cards.append(p2.pop(0))
    if not (cards[0] > len(p1) or cards[1] > len(p2)):
        #new recursive game to determine winner
        winner = recursive_lists(p1[:cards[0]],p2[:cards[1]], [], [])
        #if cards[1] > cards[0]:
        #    cards = [cards[1],cards[0]]
        if winner == 1:
            p1.extend(cards)
        else:
            p2.extend([cards[1],cards[0]])
    else:
        #normal game
        if cards[0] > cards[1]:
            p1.extend(cards)
        else:
            p2.append(cards[1])
            p2.append(cards[0])
    return recursive_lists(p1,p2,p1_decks, p2_decks)

def recursive_three(p1 = [], p2 = [], decks = set()):
    '''
    recursive game
    returns: 1 on player1 win
             2 on player2 win
    '''
    while(len(p1) > 0 and len(p2) > 0):
    
        if (tuple(p1),tuple(p2)) in decks:
            return 1
        decks.add((tuple(p1),tuple(p2)))
    
        cards = []
        cards.append(p1.pop(0))
        cards.append(p2.pop(0))
        if not (cards[0] > len(p1) or cards[1] > len(p2)):
            #new recursive game to determine winner
            winner = recursive_three(p1[:cards[0]],p2[:cards[1]], set())
            #if cards[1] > cards[0]:
            #    cards = [cards[1],cards[0]]
            if winner == 1:
                p1.extend(cards)
            else:
                p2.extend([cards[1],cards[0]])
        else:
            #normal game
            if cards[0] > cards[1]:
                p1.extend(cards)
            else:
                p2.append(cards[1])
                p2.append(cards[0])

    if p1 == []:
        return 2
    if p2 == []:
        return 1
if __name__ == "__main__":

    test_input = parse(testfile)
    input = parse(filename)

    #print(part1(test_input))
    print(part2(test_input))

    #print(part1(input))
    print(part2(input))
