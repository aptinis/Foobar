
def solution(s):

    no_leftovers = []

    for elem in range(1, len(s)+1):

        sub_string = s[:elem]
        num_slices = s.count(sub_string)

        if len(s) == (num_slices*len(sub_string)):
            no_leftovers.append(num_slices)
            
    return max(no_leftovers)