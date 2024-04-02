"""
Title: EECS 210 Assignment 5
Description: Python code for Assignment 5
Author: Kevinh Nguyen
Date: 21 March 2024
"""
print("Program 1")


def is_function(relation): 
    """
    About: function for composite using iteration for both input sets to create the composition set 
    Input: Type: R and Set of <Set> type
    Return: Type: boolean
    """
    #input variables into sets
    domain = set() 
    codomain = set() 

    #check through each pair
    for pair in relation: 
        #if domain is alr used, then not function
        if pair[0] in domain: 
            return False
        domain.add(relation[0])
        codomain.add(relation[1])
    
    #return true if each input has 1 output
    return True
        
def is_injective(relation):
    """
    About: says true or fale if ordered pairs are injective
    Input: set of ordered paris
    Return: boolean
    """
    #initialize compared codomain
    comparedCodomain = set()

    # For all elements in codomain, are they assigned to no more than one element
    for pair in relation:
        comparedCodomain.add(pair[1])

    # If codomain size = pairs, it's injective
    return len(comparedCodomain) == len(relation)

def is_surjective(relation, codomain): 
    """
    About: says true or false if ordered pairs are surjective
    Input: set of ordered pairs, set 
    Return: boolean
    """
    #initialize compared codomain

    comparedCodoomain = set() 

    #add each codomain from the function
    for pair in relation: 
        comparedCodoomain.add(pair[1])

    #if they are the codomain and compared are the same, is surjective
    return comparedCodoomain == set(codomain)



def is_bijective(relation, codomain): 
    """
    About: says true or false if ordered pairs are bijective
    Input: set of pairs, set
    Return: boolean
    """
    #if function and injective and surjective => is bijective
    return is_function(relation) and is_injective(relation) and is_surjective(relation, codomain)


def inverseFunction(relation): 
    """
    About: takes relation and spits the inverse function 
    Input: set of ordered pairs
    Return: set of ordere pairs
    """
    #flips the ordered pair (a,b) -> (b,a)
    inverse = set()
    for pair in relation: 
        inverse.add((pair[1],pair[0]))
    return inverse

def printRelations(relation, domain, codomain): 
    """
    About: prints the ordered pairs and da domain and da codomain
    input: set of ordered pair, set, set 
    Return: null
    """
    print(f"\tA = {set(domain)}")
    print(f"\tB = {set(codomain)}")
    print(f"\tf = {set(relation)}")

    # intialize list of relations
relations = [
    {"A": ["a", "b", "c", "d"], "B": ["v", "w", "x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")]},
    {"A": ["a", "b", "c", "d"], "B": ["x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "z")]},
    {"A": ["a", "b", "c", "d"], "B": ["w","x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4, 5], "f": [("a", 4), ("b", 5), ("c", 1), ("d", 3)]},
    {"A": ["a", "b", "c"], "B": [1, 2, 3, 4], "f": [("a", 3), ("b", 4), ("c", 1)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3], "f": [("a", 2), ("b", 1), ("c", 3), ("d", 2)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4], "f": [("a", 4), ("b", 1), ("c", 3), ("d", 2)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4], "f": [("a", 2), ("b", 1), ("c", 2), ("d", 3)]},
    {"A": ["a", "b", "c"], "B": [1, 2, 3, 4], "f": [("a", 2), ("b", 1), ("a", 4), ("d", 3)]}
]

#loop through each relation list and get the problem number 

for problemNumber, relationData in enumerate(relations): 
    A = relationData["A"]
    B = relationData["B"]
    f = relationData["f"]

    print(f"{problemNumber}:\n") 
    printRelations(f, A, B)
    if is_function(f): #check function
        print("\n\tThis relation is a function.")
        if is_bijective(f, B): #if both injective and surjective
            print("\tIt is bijective.")
            print("\n\tThe inverse function is:\n")
            printRelations(inverseFunction(f), B, A)
        else:
            if is_injective(f): #if only injective
                print("\tIt is injective.")
            
            if is_surjective(f, B):#if only surjective
                print("\tIt is surjective.") 
        
    else: #doesn't fit a function
        print("\n\tThis relation is not a function.")
        
print("Program 2") 
possibleNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]#inefficient but easy way to not type cast from ints to string

def readSodoku(SodokuName):
    """
    About: take in inputfile and spit out a sodoku
    Input: string 
    Return: list of lists
    """
    #initialize sodoku
    sodoku = [] 
    sodokuFile = open(SodokuName, "r")#read da file
    for line in sodokuFile:# go through each line
        #add sodoku lines
        sodokuLine = []#make list for horizontal line
        for element in line.split(): 
            sodokuLine.append(element) #add elements to horizontal line
        sodoku.append(sodokuLine)#add horizontal line to sodoku

    return sodoku #return sodoku 

#hi Junyi, how ya doing ^--^

def checker(sodoku, rowNumber, columnNumber, targetNumber): 
    """
    About: check if desired sodoku move is legal 
    Input: list of lsit, int, int, str
    Return: boolean
    """
    row = sodoku[rowNumber] 
    col = []
    for i in range(9): #add all values of the column 
        col.append(sodoku[i][columnNumber])

    #check row and column
    if (targetNumber in row)or (targetNumber in col): 
        return False #no good
    return True #yasss 

def mark(sodoku, row, column, targetNumber):
    """
    About: modify the sodoku with placed number
    Input: list of list, int, int, str
    Return: None
    """
    sodoku[row][column] = targetNumber

def printSodoku(sodoku): 
    """
    About: print da SODOKU
    Input: list of list
    Return: None
    """
    for row in sodoku: 
        print(" ".join(row))#dis is why i stopped casting, so i could use join
    print()

def find(sodoku):
    """
    About: find next missing spot, left to right, top to bottom
    Input: list of lsit
    Return: None or ordered pair
    """
    for i in range(9): 
        for j in range(9): #check entire range of sodoku
            if sodoku[i][j] == "_": #find empty spot
                return i,j #bring coordinate of empty spot
    return None #no empty spot!  sodoku filled out

def solveSodoku(sodoku): 
    """
    About: solve da sodoku with recursion and back trackign
    Input: list of list
    Return: boolean #because it do be recursing
    """
    finds = find(sodoku) #find next spot to check 
    if not finds: #all filled out! 
        return True #we are done!!
    else: #not done :(
        row, cols = finds #find next spot 
        for number in possibleNumbers: #check all numbers from 1-9
            if checker(sodoku,row,cols,number): #check if i number is good
                mark(sodoku,row,cols,number) #mark it! 
                if solveSodoku(sodoku): #pass it on 
                    return True #pass true if everyone ahead is good 
            mark(sodoku,row,cols, "_")#no numbers worked...gotta back up yall
    return False#backed up all the way, there is no solution 


"""
just a lot of printing and calling function, 

please have mercy and don't make me comment on it
"""
sodoku1 = readSodoku("KevinhNguyen_Assignment5/puzzle1.txt")
print("puzzle1.txt")
printSodoku(sodoku1)
if solveSodoku(sodoku1):
    printSodoku(sodoku1)
else:
    print("No solution")

print("Soduku2")
sodoku2 = readSodoku("KevinhNguyen_Assignment5/puzzle2.txt")
print("puzzle2.txt")
printSodoku(sodoku2)
if solveSodoku(sodoku2):
    printSodoku(sodoku2)
else:
    print("No solution")

sodoku3 = readSodoku("KevinhNguyen_Assignment5/puzzle3.txt")
print("puzzle3.txt")
printSodoku(sodoku3)
if solveSodoku(sodoku3):
    printSodoku(sodoku3)
else:
    print("No solution")

sodoku4 = readSodoku("KevinhNguyen_Assignment5/puzzle4.txt")
print("puzzle4.txt")
printSodoku(sodoku4)
if solveSodoku(sodoku4):
    printSodoku(sodoku4)
else:
    print("No solution")


sodoku5 = readSodoku("KevinhNguyen_Assignment5/puzzle5.txt")
print("puzzle5.txt")
printSodoku(sodoku5)
if solveSodoku(sodoku5):
    printSodoku(sodoku5)
else:
    print("No solution")