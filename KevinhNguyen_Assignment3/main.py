"""
Title: EECS 210 Assignment 3
Description: Python code for demonstrating operations on relations and properties of
relations
Author: Kevinh Nguyen
Date: 22 February 2024

"""

#initialize sets 
R1 = {(1,1), (2,2), (3,3)}
R2 = {(1,1), (1,2), (1,3), (1,4)}

#initialize relations
R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}

def composite(R,S): 
    """
    About: function for composite using iteration for both input sets to create the composition set 
    Input: Type: R and Set of <Set> type
    Return: Type: set composition of R and S
    """
    result = set() #init set
    for a,b in R: #iterates through first set
        for c,d in S: #iterates through second
            if b == c: #checks if coords are connected
                result.add((a,d)) #adds composite coord
    #(a,b) + (b, d) ==> (a,d)
    return result

def Reflexive(R):
    """
    About: function for reflexivity of set through iterating through each element
    Input: <Set> type R
    Output: List
    """
    reflexiveSet = list()
    for (a,b) in R: #iterates through each element
        if (a,a) not in R: #checks reflexivity
            return [False, [a,a], [b,b]] 
        else: #adds reflexive elements to set
            reflexiveSet.append((a,a))
            reflexiveSet.append((b,b))  
    return [True, reflexiveSet]

def Symmetric(R): 
    """
    About: function for checking symmetry by iterating through each (a,b) to find a (b,a) in the set
    Input: <Set> type R
    Output: List
    """
    symmetricSet = list()
    for (a,b) in R: 
        if (b,a) not in R: #checks symmetry
            return [False, [(b,a)]]
        else: #adds symmetrical coords
            symmetricSet.append([(a,b),(b,a)])
    return [True,symmetricSet]

def Antisymmetric(R):
    """
    About: function for checking antisymmetry by iterating through each (a,b) to find if (b,a) exists in the set
    Input: <Set> type R
    Output: List
    """
    antisymmetricSet = list()
    for (a,b) in R:
        if (b,a) not in R and a != b: #exclude symmetrical coordinates
            return [False, (b,a)]
        else:#adds antisymmetric coords
            antisymmetricSet.append([(a,b),(b,a)])
    return [True, antisymmetricSet]

def Transitive(R): 
    """
    About: function to check if a set is symmetrical by checking for (a,b) and (c,d) and where b==c and (a,d) exists
    Input: <Set> type R
    Output: List
    """
    transitiveSet = list()
    for (a,b) in R: #iterates through first set
        for (c,d) in R: #iterates through second set
            if b == c and (a,d) not in R: #checks for transivity
                return [False, (a,d)]
            else:
                transitiveSet.append([(a,b),(c,d),(a,d)])
                
    return [True,transitiveSet]

def setBuilder(): 
    """
    About: Built set R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}
    Input: none
    Output: <Set> type solution R
    """
    setR = set()

    for x in range(-10,11,1): #builds set as to requirements
        for y in range(-10,11,1): #builds set as to requirements
            if x + y == 0: #qualifier statement
                setR.add((x,y)) #adds to set
    return setR 



#Call Functions and Output them 

setR = setBuilder()

print("1.A R1 ∪ R2 =", R1.union(R2))
print("1.B R1 ∩ R2 =", R1.intersection(R2))
print("1.C R1 − R2 =", R1.difference(R2))
print("1.D R2 − R1 =", R2.difference(R1))
print("2 S ◦ R, = ", composite(S,R))
print("3 R^2 = ", composite(R,R))
print("4.A Show R as a set of ordered pairs =", setR)
print("4.B Show whether R is reflexive or not =", Reflexive(setR))
print("4.C Show whether R is symmetric or not =", Symmetric(setR))
print("4.D Show whether R is antisymmetric or not =", Antisymmetric(setR))
print("4.E Show whether R is transitive or not =", Transitive(setR))

