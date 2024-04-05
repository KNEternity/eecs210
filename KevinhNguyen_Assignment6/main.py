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
    print("\nForward Steps")
    while y != 0:
        r = x % y 
        divides = x // y 
        bezoutLines.append([x, y, divides, r])
        print("%s = %s * %s + %s" % (x, y, divides, r))
        x = y  # Update x to y
        y = r  # Update y to remainder

    gcd = x 
    bezoutLines.pop()
    bezoutLines.reverse()

    print("\nBackward steps:")
    a,b,c,d = bezoutLines[0]
    c1 = c
    c2 = c
    s, t = 0, 1
    for i in range(len(bezoutLines)):
        if i + 1 < len(bezoutLines):
            a_next, b_next, c_next, d_next = bezoutLines[i + 1]
            s, t = t, s - c_next * t
            if i % 2 == 0:
                print(f"{gcd} = {c1} * {a} - {c2} * {b}")
                print(f"{gcd} = {c1} * {a} - {c2} * ({a_next} - {c_next} * {a})")
            else:
                print(f"{gcd} = {c1} * {a} - {c2} * {b}")
                print(f"{gcd} = {c1} * ({a_next} - {c_next} * {a}) - {c2} * {b}")
            c1 = c1 + c_next
            c2 = c2 + c2
            a = b_next
            b = a_next
            
            
    print(f"{gcd} = {c2} * {b} - {c1} * {a}")
    print()



def main():
    print("="*10 + "PROBLEM 1" + "="*10)
    printGCD(252,198)
    printGCD(6,14)
    printGCD(24,36)
    printGCD(12,42)
    printGCD(252,198)
    print("="*10 + "PROBLEM 2" + "="*10)
    bezoutGCD(414,662)
    bezoutGCD(6,14)
    bezoutGCD(24,36)
    bezoutGCD(12,42)
    bezoutGCD(252,198)


    return 

main() 