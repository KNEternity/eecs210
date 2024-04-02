'''
Name: EECS 210 Assignment 1
Description: Python code for truth tables of logical equivalences of 6 propositions
Collaborators: Kevinh Nguyen 
Creation Date: 25 January 2024
'''


def printDeMorganFirst(): 
  '''
  About: De Morgan's first law truth table print 
  parameters: none
  return type: none
  '''
  print("="*100) #print divider line 
  print("1. De Morgan's First Law") #title of truth table
  print("P\t\tQ\t\t¬P\t\t¬Q\t\tP ∧ Q\t\t¬(P ∧ Q)\t¬P v ¬Q") #header of truth table 
  for p in [True, False]: #iterate through each bool for P and Q 
    for q in [True, False]:
      #stores the bool values for print statement
      result1 = p and q 
      result2 = not(p and q)
      result3 = not p or not q
      #prints values with respect to header of truth table 
      print(f"{p}\t\t{q}\t\t{not p}\t\t{not q}\t\t{result1}\t\t{result2}\t\t{result3}")

def printDeMorganSecond(): 
  '''
  About: De Morgan's second law truth table print 
  parameters: none
  return type: none
  '''
  print("="*100) #print divider line 
  print("2. De Morgan's Second Law") #title of truth table
  print("P\t\tQ\t\t¬P\t\t¬Q\t\tP ∨ Q\t\t¬(P ∨ Q)\t¬P ∧ ¬Q") #header of truth table 
  for p in [True, False]: #iterate through each bool for P and Q 
    for q in [True, False]:
      #stores the bool values for print statement
      result1 = p or q 
      result2 = not(p or q)
      result3 = not p and not q
      #prints values with respect to header of truth table 
      print(f"{p}\t\t{q}\t\t{not p}\t\t{not q}\t\t{result1}\t\t{result2}\t\t{result3}")

def printFirstAssociativeLaw(): 
  '''
  About: First Associative law truth table print 
  parameters: none
  return type: none
  '''
  print("="*100) #print divider line 
  print("3. First Associative Law") #title of truth table
  print("P\t\tQ\t\tR\t\tP ∧ Q\t\t(P ∧ Q) ∧ R\tQ ∧ R\t\tP ∧ (Q ∧ R)")#header of truth table 
  for p in [True, False]: #iterate through each bool for P, Q, and R variables
    for q in [True, False]:
      for r in [True, False]:
        #stores the bool values for print statement
        result1 = p and q 
        result2 = (p and q) and r
        result3 = q and r
        result4 = p and (q and r)
        #prints values with respect to header of truth table 
        print(f"{p}\t\t{q}\t\t{r}\t\t{result1}\t\t{result2}\t\t{result3}\t\t{result4}")


def printSecondAssociativeLaw(): 
  '''
  About:Second Associative law truth table print 
  Parameters: none
  Return type: none
  '''
  print("="*100) #print divider line 
  print("4. Second Associative Law") #title of truth table
  print("P\t\tQ\t\tR\t\tP ∧ Q\t\t(P ∨ Q) ∨ R\tQ ∨ R\t\tP ∨ (Q ∨ R)") #header of truth table 
  for p in [True, False]: #iterate through each bool for P, Q, and R variables
    for q in [True, False]:
      for r in [True, False]:
        #stores the bool values for print statement
        result1 = p or q 
        result2 = (p or q) or r
        result3 = q or r
        result4 = p or (q or r)
        #prints values with respect to header of truth table 
        print(f"{p}\t\t{q}\t\t{r}\t\t{result1}\t\t{result2}\t\t{result3}\t\t{result4}")

        
def printFifthProposition(): 
  '''
  About: print law truth table for [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T 
  Parameters: none
  return type: none
  '''
  print("="*100) #print divider line 
  print("5. [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T") #title of truth table
  print("P\t\tQ\t\tR\t\tP ∨ Q\t\tP → R\t\tQ → R\t\t[(P ∨ Q) ∧ (P → R) ∧ (Q → R)] → R") #header of truth table 
  for p in [True, False]: #iterate through each bool for P, Q, and R variables
    for q in [True, False]:
      for r in [True, False]:
        #stores the bool values for print statement
        result1 = p or q 
        result2 = not p or r
        result3 = not q or r
        result4 = not(result1 and result2 and result3) or r
        #prints values with respect to header of truth table 
        print(f"{p}\t\t{q}\t\t{r}\t\t{result1}\t\t{result2}\t\t{result3}\t\t{result4}")


def printSixthProposition(): 
  '''
  About: print law truth table for p ↔ q ≡ (p → q) ∧ (q → p)
  Parameters: none
  Return type: none
  '''
  print("="*100) #print divider line 
  print("6. P ↔ Q ≡ (P → Q) ∧ (Q → P)") #title of truth table
  print("P\t\tQ\t\tP → Q\t\tQ → P\t\t(P → Q) ∧ (Q → P)\tP ↔ Q") #header of truth table 
  for p in [True, False]: #iterate through each bool for P, Q, and R variables
    for q in [True, False]:
      #stores the bool values for print statement
      result1 = not p or q 
      result2 = not q or p
      result3 = result1 and result2
      result4 = (p and q) or (not p and not q)
      #prints values with respect to header of truth table 
      print(f"{p}\t\t{q}\t\t{result1}\t\t{result2}\t\t{result3}\t\t\t{result4}")



def main(): 
  '''
  About: Main function of program, runs all printPrograms in order, should refactor in the future to future-proof
  Parameters: none
  Return type: none
  '''
  printDeMorganFirst()
  printDeMorganSecond()
  printFirstAssociativeLaw()
  printSecondAssociativeLaw()
  printFifthProposition()
  printSixthProposition()

#run program :^)
main() 
