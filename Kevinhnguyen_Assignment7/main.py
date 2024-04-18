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

print(distguishableDistuigshable(52,4,5))

def indistuigshableDistuigshable(objects, boxes):
    """
    About: Indistinguishable objects into distinguishable boxes
    Input: objects(int of objects), boxes(int of boxes)
    Output: int of combinations  
    """
    return combinationsNoRepetition(objects + boxes - 1, objects) 

print(indistuigshableDistuigshable(10,8))