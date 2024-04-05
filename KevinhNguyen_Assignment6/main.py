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
    bezoutLines = []
    substitutions = {}
    while y != 0:
        r = x % y 
        divides = x // y 
        bezoutLines.append([x, y, divides, r])
        if r != integerA and r != integerB and r != 0: 
            substitutions[r] = "%s - %s * %s" % (x, divides, y)

        print("%s = %s * %s + %s" % (x, y, divides, r))
        x = y  # Update x to y
        y = r  # Update y to remainder
    
    gcd = x
        
    print("\nBackward steps:")
    s, t = 0, 1
    for i in range(len(bezoutLines) - 1, 0, -1):
        a, b, q, _ = bezoutLines[i]
        a_next, b_next, _, _ = bezoutLines[i - 1]
        s, t = t, s - q * t
        print(f"{gcd} = {a_next} - {q} * ({a})")

    
    print(bezoutLines)
    print(substitutions)



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