
def solution(x, y):
    '''Computes the number of regeneration cycles required to produce the desired number of mach and facula bombs. During each generation cycle the bombs can self replicate in 1 of 2 ways: for every mach bomb a facula bomb is created or for each facula bomb a mach bomb is created. 

    Args: x, y strings of positive integers with values between [1-10^50] representing the desired number of mach & facula bombs

    Returns: a string of the number of regeneration cycles required to reach the desired end state.'''
    
    x = long(x)
    y = long(y)
    counter = 0

    while x > 0:
        counter += max(x, y) // min(x, y)
        x, y = max(x, y) % min(x, y), min(x, y)

        if y != 1 and x == 0:
            return "impossible"
            
    return str(int(counter - 1))