
def solution(xs):
    ''' Finds the maximum product of a non empty subset of the array xs

    Args: a list of integers with 1 to 50 elements whose absolute values are no greater than 1000. 

    Returns: the maximum product as a string '''

    def remove_zeros_from_list(xs):
       return [i for i in xs if i != 0]

    def product(l):
        t = 1
        for x in l:
            t = t * x
        return t

    # set the intial max product as the product of the entire array
    prod = product(xs)

    # create a list of all the negative numbers
    neg_nums = [i for i in xs if i < 0]

    # if there is an odd number of negative numbers, drop the negative number with the smallest absolute value from the array
    if len(neg_nums) > 0 and len(neg_nums) % 2 == 1:
        xs.remove(min(neg_nums, key=abs))

    # remove all 0s from the array
    xs = remove_zeros_from_list(xs)

    # After dropping the 0s if the list is non empty update the maximum product
    if len(xs) > 0:
        prod = product(xs)

    return str(prod)