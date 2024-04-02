"""
Title: EECS 210 Assignment 4
Description: Python code for determining relations of sets
Author: Kevinh Nguyen
Date: 7 March 2024

"""

def isReflexive(relation, set):
    """
    Input: list, set
    Output: boolean
    About: checks if relation is reflexive against a set
    """

    for element in set: #check if an element has an ordered pair of (element, element in the set, return false if 1 DNE
        if (element,element) not in relation:
            return False
    return True #true if all elements have reflex pair

def findReflexiveClosure(relation, set):
    """
    Input: list, set
    Output: list
    About: returns a list of reflexive closure 
    """
    closure = relation.copy() #copy r into r*

    for ele in set: 
        if (ele, ele) not in relation: #add difference between r* and r to closure
            closure.append((ele,ele))
    return closure #return r*


def reflexiveOutput(relation, set):
    """
    Input: list, set 
    Output: print of strings
    About: prints whether a relation and a set is reflexive and prints difference if not
    """
    print("\t\ta) R =", relation) #prints relation
    print("\t\tb) R is reflexive:", isReflexive(relation, set))
    # If it's not reflexive it will also print it's reflexive closure
    if not isReflexive(relation, set):
        print("\t\tc) R* if not reflexive:", findReflexiveClosure(relation, set))
    return

#print problem 1
print("1.d\t")
relation1 = [(1,1),(4,4),(2,2),(3,3)]
set1 = {1,2,3,4}
reflexiveOutput(relation1,set1)

print("1.e\t")
relation2 = [("a","a"),("c","c")]
set2 = {"a","b","c","d"}
reflexiveOutput(relation2,set2)




def isSymmetric(relation):
    """
    Input: list
    Output: boolean
    About: prints bool value of whether relatino is symmetric
    """
    for (a,b) in relation: 
        if (b,a) not in relation: #checks if pair has a symmetric pair, return false if not
            return False
    return True

def findSymmetricClosure(relation):
    """
    Input: list
    Output: list
    About: creates r* from r
    """
    closure = relation.copy() #creates copy of r into r*

    for (a,b) in relation: 
        if (b,a) not in relation:
            closure.append((b,a)) #adds any missing pairs into r*
    return closure #returns r*

def symmetricOutput(relation):
    """
    Input: list
    Output: print of strings
    About: prints whether relation is symmetric
    """
    print("\t\ta) R =", relation)
    print("\t\tb) R is symmetric:", isSymmetric(relation))
    # If it's not symmetric it will also print it's symmetric closure
    if not isSymmetric(relation):
        print("\t\tc) R* if not symmetric:", findSymmetricClosure(relation))
    return 

#print problem 2
print("2.\tEx 1:")
relation1 = [(1, 2), (4, 4), (2, 1), (3, 3)]
symmetricOutput(relation1)

print("\tEx 2:")
relation2 = [(1, 2), (3, 3)]
symmetricOutput(relation2)

def isTransitive(relation,set):
    """
    Input: list, set
    Output: boolean
    About: determines whether relation is transitive compared to set
    """
    for a in set:
        for b in set: 
            for c in set: 
                #if (a,b) and (b,c) exists, then (a,c) has to exist if r is transitive, return false if not
                if ((a,b) in relation and (b,c) in relation) and (a,c) not in relation: 
                    return False
    return True 

def findTransitiveClosure(relation, set):
    """
    Input: list, set
    Output: list
    About: create transitive r* from r
    """
    closure = relation.copy() #copy r to r*
    for a in set:
        for b in set: 
            for c in set: 
                if ((a,b) in relation and (b,c) in relation) and (a,c) not in relation: 
                    closure.append((a,c)) #add any missing transitive pairs into r*
    return closure #return r*

def transitiveOutput(relation,set):
    """
    Input: list, set
    Output: print statement
    About: prints if relation is transitive compared to set
    """
    print("\t\ta) R =", relation)
    print("\t\tb) R is transitive:", isTransitive(relation, set))
    # If it's not transitive it will also print it's transitive closure
    if not isTransitive(relation, set):
        print("\t\tc) R* if not transitive:", findTransitiveClosure(relation, set))

#print problem 3
print("3.\tEx 1:")
relation1 = [('a','b'), ('d','d'), ('b','c'), ('a','c')]
set1 = {'a', 'b', 'c', 'd'}
transitiveOutput(relation1, set1)

print("\tEx 2:")
relation2 = [(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)]
set2 = {1, 2, 3}
transitiveOutput(relation2, set2)

def equivalenceOutput(relation, set):
    """
    Input: list, set 
    Output: print statements
    About: checks if relation is equivalence from set, prints reasons
    """
    print("\t\ta) R =", relation)
    if isReflexive(relation, set) and isSymmetric(relation) and isTransitive(relation, set): #ticks all equivalence conditions, print so
        print("\t\tb) R is an equivalence relation")
    else: 
        print("\t\tb) R is not an equivalence relation") #if conditions not met, print not equivalence
        if not isReflexive(relation, set): 
            print("\t\tIt is not reflexive") #not reflexive check and print
        if not isSymmetric(relation):
            print("\t\tIt is not symmetric") # not symmetric check and print
        if not isTransitive(relation, set):
            print("\t\tIt is not transitive") #not transitive check and print

#print problem 4
print("4.\tEx 1:")
relation1 = [(1, 1), (2, 2), (2, 3)]
set1 = {1, 2, 3}
equivalenceOutput(relation1, set1)

# Example 2:
print("\tEx 2:")
relation2 = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('b','c'), ('c','b')]
set2 = {'a', 'b', 'c'}
equivalenceOutput(relation2, set2)


def isAntisymmetric(relation):
    """
    Input: list 
    Output: boolean
    About: checks if list is antisymmetric, returns boolean 
    """
    for (a,b) in relation: 
        #ignores reflexive AND checks if symmetric pair exists
        if a!= b and ((b,a) in relation): 
            return False #if symmetric pair exists
    return True #else not

def posetOutput(relation, set):
    """
    Input: list, set
    Output: print statement
    About: prints whether relation is poset 
    """
    print("\t\ta) S =", set) #print set
    print("\t\tb) R =", relation) #print relation
    if isReflexive(relation, set) and isAntisymmetric(relation) and isTransitive(relation, set):  #check all conditions of poset
        print("\t\tc) (S, R) is a poset:", True) #yes if all conditions met
    else: 
        print("\t\tc) (S,R) is a poset:", False) #no if conditions not met
        if not isReflexive(relation, set):
            # If the relation isn't reflexive, state it is not reflexive
            print("\t\td) (S, R) isn't a poset because it is not reflexive")
        if not isAntisymmetric(relation):
            # If the relation isn't antisymmetric, state it is not antisymmetric
            print("\t\td) (S, R) isn't a poset because it is not antisymmetric")
        if not isTransitive(relation, set):
            # If the relation isn't transitive, state it is not transitive
            print("\t\td) (S, R) isn't a poset because it is not transitive")
    return 

#print problem 5
print("5.\tEx 1:")
relation1 = [(1,1),(1,2),(2,2),(3,3),(4,1),(4,2),(4,4)]
set1 = {1, 2, 3, 4}
posetOutput(relation1, set1)

# Example 2:
print("\tEx 2:")
relation2 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)]
set2 = {0, 1, 2, 3}
posetOutput(relation2, set2)