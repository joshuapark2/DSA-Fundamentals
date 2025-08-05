'''
The following function uses recursion to calculate the Nth number from a mathematical sequence 
known as the “Golomb sequence.” 

Its terribly inefficient, though! Use memoization to optimize it. 
(You dont have to actually understand how the Golomb sequence works to do this exercise.)
'''

def golomb(n, memo={}):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]

def golomb_my_version(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        memo[n] = 1
    if not memo.get(n):
        memo[n] = 1 + golomb_my_version(n - golomb_my_version(golomb_my_version(n - 1, memo), memo), memo)
        print(memo[n], 1 + golomb_my_version(n - golomb_my_version(golomb_my_version(n - 1, memo), memo), memo))
    return memo[n]

golomb(10)


# Given below
def golomb_inefficient(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        memo[n] = 1
    else:
        memo[n] = 1 + golomb_inefficient(n - golomb_inefficient(golomb_inefficient(n - 1, memo), memo), memo)
    return memo[n]


'''
Trying to understand:

memo[element] = 1 + golomb(n - golom(golomb(n - 1, memo), memo), memo)


golomb(n - 1, memo) -> golomb(n - result of (n - 1)) -> golomb(n - 2) -> golomb(n - result of golomb(n - 2))


n - 1 -> n - 2 -> n - (n - 2)
'''
  
