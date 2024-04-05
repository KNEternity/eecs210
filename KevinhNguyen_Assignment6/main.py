'''
Name: EECS 210 Assignment 6
Description: 
Collaborators: Kevinh Nguyen 
Creation Date: 2 April 2024
'''

def greatestCommonDivisor(integerA, integerB): 
    """
    About: finds great common divisor
    Input: 2 ints
    Output: integer
    """
    x = max(integerA, integerB) #set max value
    y = min(integerA, integerB) #set min

    while y != 0: #method from the book

        r = x % y 
        divides = x//y 
        print("%s/%s = %s R %s " % (x, y, divides, r))
        x = y 
        y = r 
    return x #dis is gcd

def printGCD(intA, intB): 
    """
    About: prints gcd how i want
    Input: 2 ints
    Output: none, print value
    """
    GCD =  greatestCommonDivisor(intA,intB)
    print("gcd(%s,%s) = %s\n" % (intA, intB, GCD))

def bezoutGCD(integerA, integerB):
    """
    About: finds GCD da bezout way and reversal
    Input: 2 ints
    Output: none print type
    """
    x = max(integerA, integerB) #same as before
    y = min(integerA, integerB)
    bezoutLines = [] #archive steps for backwards process
    print("\nForward Steps")
    while y != 0:
        r = x % y 
        divides = x // y 
        bezoutLines.append([x, y, divides, r]) #add for record purpose
        print("%s = %s * %s + %s" % (x, y, divides, r))
        x = y  # Update x to y
        y = r  # Update y to remainder

    gcd = x #init for later use 
    bezoutLines.pop() #dont need the last dividing
    bezoutLines.reverse() #go bottom up 

    print("\nBackward steps:")
    a,b,c,d = bezoutLines[0]
    c1 = 1 #set linearity 
    c2 = c
    for i in range(len(bezoutLines)):
        if i + 1 < len(bezoutLines):#dont care about the last line, just print bezout coef
            a_next, b_next, c_next, d_next = bezoutLines[i + 1] #use some of the values of the table of next row
            if i % 2 == 0:#substitute right var
                print(f"{gcd} = {c1} * {a} - {c2} * {b}")
                print(f"{gcd} = {c1} * {a} - {c2} * ({a_next} - {c_next} * {a})")
            else:#substitute left var
                print(f"{gcd} = {c1} * {a} - {c2} * {b}")
                print(f"{gcd} = {c1} * ({a_next} - {c_next} * {a}) - {c2} * {b}")
            c1 = c1 + c_next #calculate next variables in line 
            c2 = c2 + c2
            a = b_next
            b = a_next
            
            
    print(f"{gcd} = {c2} * {b} - {c1} * {a}") #print final step
    print()

def extendedEuclideanGCD(a, b):
    """
    Does the gcd(a, b) using the extended Euclidean algorithm, and finds the bezout coefficients s and t

    Inputs: 2 int

    Ouputs: 2 ints
    """

    # init var
    a0, b0 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    q_values = []

    # break if b is 0 and adds to a list of q values
    while b != 0:
        quotient = a // b
        q_values.append(quotient)

        a, b = b, a % b
        s0, s1 = s1, s0 - quotient * s1
        t0, t1 = t1, t0 - quotient * t1

    gcd = a
    s = s0
    t = t0

    # string comprehension for quotients
    print("\nQuotients (q values):", end=' ')
    for i, q in enumerate(q_values):
        print(f"q{i + 1} = {q}", end=', ' if i < len(q_values) - 1 else '\n')

    # s Values
    print("\nCalculations for s values:\n")
    for i in range(len(q_values)):
        print(f"s{i} = {1 if i == 0 else 0} - {1 if i == 1 else 0} * {q_values[i]} = {s0 if i == 0 else 0 - q_values[i] * s1}")

    # t values
    print("\nCalculations for t values:\n")
    for i in range(len(q_values)):
        print(f"t{i} = {0 if i == 0 else 1} - {0 if i == 1 else 1} * {q_values[i]} = {t0 if i == 0 else 1 - q_values[i] * t1}")

    # gcd expressed with bezout's coefficients
    print(f"\ngcd({a0}, {b0}) = {gcd} = {s}*{a0} + {t}*{b0}")


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
    print("="*10 + "PROBLEM 3" + "="*10)
    extendedEuclideanGCD(414,662)
    extendedEuclideanGCD(6,14)
    extendedEuclideanGCD(24,36)
    extendedEuclideanGCD(12,42)
    extendedEuclideanGCD(252,198)

    return 

main() 