

def solution(l):

    '''Computes the number of lucky triples in list l, where a lucky triple is a tuple (li, lj, lk) where li divides lj and lj divides lk with indices i < j < k. 
    Args: list of positive integers l with values [1-999999] and length [2-2000]
    Returns: an integer of the total number of lucky triple combinations within the list'''

    # initialize an array to store the number of divisors each element of the list has. 
    num_divisors = len(l)*[0]
    # initialize the number of lucky triples in the list
    num_triples = 0

    # traverse the array & check if each previous list element divides the current list element k
    for k in range(1, len(l)):
        for j in range(k):
            
            if l[k] % l[j] == 0:
                # if lk is divided by lj add 1 to the number of divisors for lk
                num_divisors[k] = num_divisors[k] + 1
                # a lucky triple is formed if the new divisor of lk (lj) also has a divisor
                # Add the number of divisors lj has to the lucky triple count.
                num_triples = num_triples + num_divisors[j]

    return num_triples