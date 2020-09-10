
def solution(n):
    ''' Computes the number of different staircases that
    can be built from exactly n bricks. Staircases must be
    at least 2 steps. Each step must be lower than the previous
    one and contain at least 1 brick. 
    Args: positive integer n between [3, 200]
    Returns: positive integer of the number of different staircases
        '''
    arr = range(1, n)
    dp = [ [0]*(n+1) for i in range(len(arr))]

    for i in range(len(dp)):
        dp[i][0] = 1

    for i in range(len(arr)):
        for j in range(n+1):
            if j >= arr[i]:
                dp[i][j] = dp[i-1][j-arr[i]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return int(dp[-1][-1])