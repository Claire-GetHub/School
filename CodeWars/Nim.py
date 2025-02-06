#NOT DONE

def choose_move(gs):
    pile = None
    amount = None
    nonEmpty = nonEmptyPiles(gs)
    nonOne = nonOnePiles(gs)
    uq = uniqueValues(nonEmpty)
    
    #check if its the last move 
    if (len(nonEmpty) == 1 
        #or take a full pile if none are diffrent and there are more than 2 piles
        or len(uq) == 0 and len(nonEmpty) > 2
        #or there are only ones
        or (len(nonOne) == 0 and len(nonEmpty) > 2)):
        print("grab first pile")
        pile = [*nonEmpty.keys()][0]
        amount = nonEmpty[[*nonEmpty.keys()][0]]
    
    #take pile that is diffrent
    elif len(uq) == 1:
        print("grab unique pile")
        pile = [*uq.keys()][0]
        amount = uq[[*uq.keys()][0]]
    elif len(nonOne) == 1:
        print("grab non one pile")
        leave = 1 if len(nonEmpty) > 2 and nonOne[[*nonOne.keys()][0]] != 2 else 2
        pile = [*nonOne.keys()][0]
        amount = nonOne[[*nonOne.keys()][0]] - leave
    elif len(uq) == 0:
        print("leave one in a pile")
        pile = [*nonEmpty.keys()][0]
        amount = nonEmpty[[*nonEmpty.keys()][0]] - 1

    return pile, amount


def nonEmptyPiles(gs):
    nonEmpty = {i:gs[i]  for i in range(len(gs)) if gs[i] != 0}
    return nonEmpty

def nonOnePiles(gs):
    nonOne = {i:gs[i]  for i in range(len(gs)) if gs[i] != 1 and gs[i] != 0}
    return nonOne

def uniqueValues(nonEmpty):
    uniq = {}
    for key in nonEmpty:
        copy = nonEmpty.copy()
        copy.pop(key)
        if not nonEmpty[key] in copy.values():
            uniq[key] = nonEmpty[key]
    return uniq


nonEmpty = nonEmptyPiles([0,0,3,3,5])
print(choose_move([0,0,0,1,2]))
#1