#NOT DONE

def choose_move(gs):
    pile = None
    amount = None
    nonEmpty = nonEmptyPiles(gs)
    nonOne = nonOnePiles(gs)
    uq = uniqueValues(nonEmpty)
    
    #take pile that is different
    if len(nonEmpty) == 2 and nonEmpty[max(nonEmpty, key=nonEmpty.get)] != nonEmpty[min(nonEmpty, key=nonEmpty.get)]:
        print("even out piles")
        leave = 2 if nonEmpty[min(nonEmpty, key=nonEmpty.get)] == 1 and nonEmpty[max(nonEmpty, key=nonEmpty.get)] != 2 else nonEmpty[min(nonEmpty, key=nonEmpty.get)]

        pile = max(nonEmpty, key=nonEmpty.get)
        amount = nonEmpty[max(nonEmpty, key=nonEmpty.get)] - leave
    elif len(nonOne) == 1 or len(nonEmpty) == 2 :
        print("main logic")
        if  (len(nonEmpty) - 1) % 2 == 0:
            leave = 0
        else:
            leave = 1
        print(leave)
        pile = [*nonEmpty.keys()][0]
        amount = nonEmpty[[*nonEmpty.keys()][0]] - leave
    elif len(uq) == 1:
        print("grab unique pile")
        pile = [*uq.keys()][0]
        amount = uq[[*uq.keys()][0]]
    # elif len(uq) == 0:
    #     print("leave one in a pile")
    #     pile = [*nonEmpty.keys()][0]
    #     amount = nonEmpty[[*nonEmpty.keys()][0]] - 1
    else:
        pile = [*nonEmpty.keys()][0]
        amount = nonEmpty[[*nonEmpty.keys()][0]]

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


print(choose_move([0, 1,2]))
