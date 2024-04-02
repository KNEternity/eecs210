'''
Name: EECS 210 Assignment 2
Description: Python code for 210 Assignment 2
Collaborators: Kevinh Nguyen 
Creation Date: 29 January 2024
'''


domain = [0,1,2,3,4,5,6,7,8,9,10]
secondDomain = [1,2,4,5,10,0.5,0.25,0.2,0.1]
def printLine(): 
  '''
  About: prints lines between problems
  parameters: none
  return type: none
  '''
  print("="*50)

def problemOneA(): 
  '''
  About: solves the first problem 
  parameters: none
  return type: none
  '''
  printLine()
  print("Problem 1.A")
  for x in domain: #covers 0-10
    if x < 2: #checks if there exists x<2
        print("True : %s" % (x)) #output
        return #break since assertion solved
    else: 
        print("False: %s" % (x)) #print if case is false
      
def problemOneB(): 
    '''
    About: solves the second problem
    parameters: none
    return type: none
    '''
    printLine()
    print("Problem 1.B")
    for x in domain: #covers 0-10
        if not x < 2: #checks if statement is wrong
            print("False: %s" % (x)) #1 case proven wrong so break
            return
        
    else: 
        print("True: %s" % (x)) #print if case is true
        
def problemOneC(): 
    '''
    About: solves ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is
    the statement “x>7”

    parameters: none
    return type: none
    '''
    printLine()
    print("Problem 1.C")
    for x in domain: #covers domain 0-10
        if  (x < 2) and (x > 7): #checks conjoint statements
            print("True: %s" % (x)) #output answer
            return
    else: 
        print("False: %s" % (x)) #output answer

def problemOneD(): 
    '''
    About: solves ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is
    the statement “x>7”

    parameters: none
    return type: none
    '''
    printLine() #print line
    print("Problem 1.D") #print problem
    for x in domain: #covers 0-10
        if not ((x < 2) or (x > 7)): #find 1 case of false
            print("False: %s" % (x)) #output result
            return
    else: 
        print("True: %s" % (x)) #output result

        
def problemOneE(): 
    '''
    About: Prove De Morgan’s Law for the Existential Quantifier where P(x) is
    the statement “x<5”

    parameters: none
    return type: none
    ''' 
    printLine()
    print('1.E')

    for x in domain: #covers 0 - 10 | negated statement
        if not(x < 5):  # find 1 case of false negated statement

            print("Negated statement is True: %s" % (x)) #output result
            negated = True #used to check original 
            break


    for x in domain: #covers 0-10 | original statement
        if not x < 5: #checks if original statement is wrong 
            pvirint("Original is True: %s" % (x)) #True since we negated it 
            original = True #used to check against negated statement
            break

    if negated == original: #check if both statements are equal
        print("Since original and negated are equal, De Morgan's Law for Existenial Quantifiers Holds")


def problemOneF():
    '''
    About: Prove De Morgan’s Law for the Universal Quantifier where P(x) is the
    statement “x<5” evals to true
    parameters: none
    return type: none
    '''    
    printLine()
    print("Problem 1.F")
    for x in domain: #covers 0 - 10 | negated statement
        if not (x < 5):  # find 1 case of negated statement

            print("Negated statement is True: %s" % (x)) #output result
            negated = True #used to check original 
            break


    for x in domain: #covers 0-10 | original statement
        if not x < 5: #checks if original statement is wrong 
            print("Original is True: %s" % (x)) #True since we negated it 
            original = True #used to check against negated statement
            break

    if negated == original: #check if both statements are equal
        print("Since original and negated are equal, De Morgan's Law for Universal Quantifiers Holds")



def problemTwoA():
    '''
    About: solves ∀x∀yP(x,y)
    parameters: none
    return type: none
    ''' 
    Find = False #find if condition works
    printLine()
    print("Problem 2.A")
    for x in secondDomain: #domain for x
        for y in secondDomain: #domain for y 
            if not((x*y) == 1): #check for 1 false case
                find = True #flip to break out of loop
                print("False: x = %s, y = %s" %(x,y))#print result
                break
        if find: #break again since case has been found 
            break
    return 


def problemTwoB(): 
    '''
    About: solves ∀x∃yP(x,y)
    parameters: none
    return type: none
    '''
    Find = False
    printLine()
    print("Problem 2.B")
    for x in secondDomain: #domain for x
        for y in secondDomain: #domain for y
            if (x*y) == 1: #find 1 case where this is true
                Find = True
                break
        if not Find: #if suitable Y NOT FOUND
            print("False: x = %s, y = %s" % (x,y)) #output result
            return
    print("True for all X and Y") #output results
    return 

def problemTwoC(): 
    '''
    About: solves ∀y∃xP(x,y)
    parameters: none
    return type: none
    '''
    find = False #init
    printLine()
    print("Problem 2.C")
    for y in secondDomain: 
        for x in secondDomain: 
            if (y*x) == 1: #find 1 existential case if true 
                find = True
                break
        if not find: #found so break
            print("False: y = %s, x = %s" % (y,x))
            break
    print("True for all X and Y")
    return 

def problemTwoD(): 
    '''
    About: ∃x∀yP(x,y)
    parameters: none
    return type: none
    '''
    find = False
    printLine()
    print("Problem 2.D")
    for x in secondDomain: 
        for y in secondDomain: 
            if (x*y) != 1: #find 1 false case 
                find = True
                break
        if find: #break out
            break
        else:
            print("True: x = %s, y = %s" % (x,y))
            break
    print("False: x = %s, y = %s" % (x,y))
    return 

def problemTwoE():
    '''
    About: ∃y∀xP(x,y)
    parameters: none
    return type: none
    '''
    find = False
    printLine()
    print("Problem 2.E")
    for y in secondDomain: 
        for x in secondDomain: 
            if (x*y) != 1: #find 1 false case 
                find = True
                break
        if find: 
            break
        else: #all x's work for 1 y
            print("True: all x's, y = %s" % (y))
            break
    print("False: x = %s, y = %s" % (x,y)) #output results
    return 

def problemTwoF(): 
    '''
    About: ∃x∃yP(x,y)
    parameters: none
    return type: none
    '''
    find = False
    printLine()
    print("Problem 2.F")
    for y in secondDomain: 
        for x in secondDomain: 
            if (x*y) == 1: #find 1 true case
                find = True
                print("True: x = %s, y = %s" % (x,y))
                break
        if find:
            break
        else:
            print("False: x = %s, y = %s" % (x,y))
            break
    return 


def main(): 
    '''
    About: run main
    parameters: none
    return type: none
    '''
    problemOneA()
    problemOneB()
    problemOneC()
    problemOneD()
    problemOneE()
    problemOneF()
    problemTwoA()
    problemTwoB()
    problemTwoC()
    problemTwoD()
    problemTwoE()
    problemTwoF()
    return

main()