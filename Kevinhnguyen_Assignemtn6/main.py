'''
Name: EECS 210 Assignment 6
Description: 
Collaborators: Kevinh Nguyen 
Creation Date: 2 April 2024
'''

def greatestCommonDivisor(integerA, integerB): 
    """
    About
    Input: 
    Output: integer
    """
    x = max(integerA, integerB)
    y = min(integerA, integerB)

    while y != 0:
        r = x % y 
        divides = x//y 
        print("%s/%s = %s R %s " % (x, y, divides, r))
        x = y 
        y = r 
    return x

def printGCD(intA, intB): 
    GCD =  greatestCommonDivisor(intA,intB)
    print("gcd(%s,%s) = %s\n" % (intA, intB, GCD))

def bezoutGCD(integerA, integerB):
    x = max(integerA, integerB)
    y = min(integerA, integerB)
    while y != 0:
        r = x % y 
        divides = x//y 
        print("%s = %s * %s + %s " % (x, y, divides, r))
        x = y #=GCD at the end
        y = r #=0 at the end

    print(y) 
    


def main():
    print("="*10 + "PROBLEM 1" + "="*10)
    printGCD(252,198)
    printGCD(6,14)
    printGCD(24,36)
    printGCD(12,42)
    printGCD(252,198)
    print("="*10 + "PROBLEM 2" + "="*10)
    bezoutGCD(252,198)


    return 

main() 