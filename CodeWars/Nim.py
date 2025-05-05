#NOT DONE

def choose_move(gs):
    pile = None
    amount = None
    nonEmpty = nonEmptyPiles(gs)
    nonOne = nonOnePiles(gs)
    uq = uniqueValues(nonEmpty)
    if len(nonOne) != 0:
        large = max(nonOne, key=nonOne.get)
        small = min(nonOne, key=nonOne.get)
    else:
        #make large and small diffrent variables
        ...

    key0 = [*nonEmpty.keys()][0]
    
    #take pile that is diffrent
    if len(nonOne) == 2 and large != small:
        print("even out piles")

        pile = large
        amount = nonEmpty[large] - nonEmpty[small]
    elif len(nonEmpty) == 2 or len(nonOne) == 1:
        print("leave 0 or 1")
       
        leave = (len(nonEmpty) - 1) % 2


        pile = large
        amount = nonEmpty[large] - leave
    elif len(uq) == 1:
        print("grab unique pile")
        pile = [*uq.keys()][0]
        amount = uq[[*uq.keys()][0]]
    else:
        pile = key0
        amount = nonEmpty[key0]

    print(gs)
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


print(choose_move([2, 3, 1]))