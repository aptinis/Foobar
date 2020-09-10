
def find_min(total_lambs):
    ''' Find the minimum number of henchman you can pay given total lambs
    Args: integer value of the total total_lambs to distribute
    Returns: integer representing the minimum number of henchmen you can pay
    '''

    # there will always be a henchman who will also always be paid 1 lambs
    henchman = [1]
    spent_lambs = 0

    while spent_lambs < total_lambs:
        # the most you can pay a henchman is double the previous rank henchman
        henchman.append(henchman[-1]*2)
        # find the total lambs spent so far
        spent_lambs = sum(henchman)
        # if adding the next rank brings you over the total lambs remove

        if spent_lambs > total_lambs:
            henchman = henchman[:-1]

    return len(henchman)

def find_max(total_lambs):
    '''Find the maxium number of henchman you can pay given total lambs
    Args: integer value of the total lambs to distribute
    Returns: integer value of maximum number of henchmen you can pay'''

    # there will always be a henchman who will also always be paid 1 lambs
    henchman = [1]
    # intialize the total money distributed so far
    spent_lambs = 0

    while spent_lambs < total_lambs:
        # the second most junior rank does not have 2 junior subordinates and can't make less than most junior. 

        if len(henchman) == 1:
            henchman.append(1)
        else:
            # the least you can pay a henchmen is combined total from 2 more junior henchmen
            henchman.append(henchman[-1] + henchman[-2])
            # find total lambs spent so far
            spent_lambs = sum(henchman)
        # if adding the next rank brings you over the total lambs remove
        if spent_lambs > total_lambs:
            henchman = henchman[:-1]
            
    return len(henchman)

def solution(total_lambs):
    ''' Finds the difference between the maximum and minium number of henchmen you can pay given total lambs to distribute.
    Args: total lambs to distribute (positive integer less than 1 billion)
    Returns: difference between the the maximum and minimum number of henchmen as an integer.
    '''
    return find_max(total_lambs) - find_min(total_lambs)