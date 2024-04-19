"""
EECS210 Assignment 7
Description:
Full Name: Kevinh Nguyen
Creation Date: 04/17/24
"""
from math import factorial

def combinationsNoRepetition(n, k):
    """
    About: Combinations without repetition
    Input: n(number of objects), k(number of boxes) 
    Output: Number of combinations without repitition
    """
    return factorial(n) // (factorial(k) * factorial(n - k))


def distguishableDistuigshable(objects, amt, boxes):
    """
    About: Distinguishable objects into distinguiable boxes 
    Input: objects(int of objects), amt(int of objects per box), boxes (int of boxes) 
    Output: int of combinations 
    """
    result = 1 # Initialize var to represent the result
    while amt > 0: # Iterate through the range of amt
        result *= combinationsNoRepetition(objects, boxes) # Multiply the result by the number of combinations without repetition
        objects -= boxes # Subtract boxes from objects
        amt -= 1 # Decrement amt
    return result


def indistuigshableDistuigshable(objects, boxes):
    """
    About: Indistinguishable objects into distinguishable boxes
    Input: objects(int of objects), boxes(int of boxes)
    Output: int of combinations  
    """
    return combinationsNoRepetition(objects + boxes - 1, objects) 


def stirling_second(n, j):
    """
    About: Stirling numbers of the second kind
    Input: n(int of objects), j(int of boxes) 
    output: combinations(int) 
    """
    summation = 0 # Initialize var to represent summation of the terms
    for i in range(0, j): # Iterate through the range of i from 0 to j
        summation += combinationsNoRepetition(j,i)*((j-i)**n)*((-1)**i) # Add the term to the summation
    result = summation//factorial(j) # Divide the summation by j factorial
    return result
        
def distguishableIndistuighable(n, k):
    """
    About: calculate distuigshable objects into indistuighable boxes 
    Input: object n(int), boxes k(int) 
    Output: cominations(int) 
    """
    term = 0 # Initialize var to represent the term
    for j in range(1, k + 1): # Iterate through the range of j from 1 to k + 1
        term += stirling_second(n, j) # Add the term to the jth Stirling number of the second kind
    return term # Return the term
    
def pk(n, k): 
    """
    About: number of partitions needed for a certain of boxes n
    Input: objects n(int), boxes k(int)
    Output: int
    """
    if n == 0 and k == 0: # Base case if n and k are both 0
        return 1
    if (n <= 0 or k <= 0): # Base case if n or k are less than or equal to 0
        return 0
    return pk(n - k, k) + pk(n - 1, k - 1) # Return the sum of the two recursive calls

def indistguishableIndistguishable(n, k):
    """
    About: number of combinations of ind,ind objects to boxes
    Input: object n(int), boxes k(int) 
    output: combinations(int) 
    """
    term = 0 # Initialize var to represent the term
    for j in range(1, k + 1): # Iterate through the range of j from 1 to k + 1
        term += pk(n, j) # Add the term to the jth partition number
    return term


#problem 1 
print("1.")
print(distguishableDistuigshable(52,4,5))
print(distguishableDistuigshable(40,4,10))

print()
print("2.")
print(indistuigshableDistuigshable(10,8))
print(indistuigshableDistuigshable(12,6))

print()
print("3.")
print(distguishableIndistuighable(4,3))
print(distguishableIndistuighable(5,4))

print()
print("4.")
print(indistguishableIndistguishable(6,4))
print(indistguishableIndistguishable(5,3))