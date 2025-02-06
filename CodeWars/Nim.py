#NOT DONE

def choose_move(gs):
    pile = None
    amount = None
    nonEmpty = nonEmptyPiles(gs)
    uq = uniqueValues(nonEmpty)
    
    #check if its the last move or take a full pile if none are diffrent and there are more than 2 piles
    if len(nonEmpty) == 1 or len(uq) == 0 and len(nonEmpty > 2):
        amount = [*nonEmpty.keys()][0]
        pile = nonEmpty[[*nonEmpty.keys()][0]]
    
    #take pile that is diffrent
    elif len(uq) == 1:
        amount = [*uq.keys()][0]
        pile = uq[[*uq.keys()][0]]


    return pile, amount


def nonEmptyPiles(gs):
    nonEmpty = {i:gs[i]  for i in range(len(gs)) if gs[i] != 0}
    return nonEmpty

def uniqueValues(nonEmpty):
    uniq = {}
    for key in nonEmpty:
        copy = nonEmpty.copy()
        copy.pop(key)
        if not nonEmpty[key] in copy.values():
            uniq[key] = nonEmpty[key]
    return uniq


nonEmpty = nonEmptyPiles([0,0,3,3,5])
