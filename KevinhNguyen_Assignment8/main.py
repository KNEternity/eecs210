"""
EECS210 Assignment 8
Description: A program for finding Euler's Circuit and telling if a circuit is a hamilton circuit using two different methods
Full Name: Kevinh Nguyen
Creation Date: 04/17/24
"""
from collections import defaultdict

#class for undirected graph 

class Graph: 
    def __init__(self): 
        self.graph = defaultdict(set) 
        
    def add_edge(self, u, v):
        """
        
        """
        self.graph[u].add(v)
        self.graph[v].add(u)
        
    def is_euler_circuit(self):
        for vertex in self.graph: 
            if len(self.graph[vertex]) % 2 != 0:
                return False
        return True 
    
    def euler_circuit(self): 
        if not self.is_euler_circuit(): 
            print("euler circuit not possible")
            print("Odd Vertexes:")
            for vertex in self.graph:
                if len(self.graph[vertex]) % 2 != 0: 
                    print(vertex)
            return 

        circuit = []
        self.euler_circuit_util(next(iter(self.graph)), circuit) #begins with the first element in the circuit
        print("\t\tEuler circuit:", end=" ")
        print('-'.join(circuit[::-1]))  # Reverse the circuit to correct the order
    
    def euler_circuit_util(self, current, circuit):
        # function to help the euler circuit function
        # Inputs
        #     current: edge
        #     circuit: list
        # Ouputs
        #     None
        neighbors = list(self.graph[current]) #list out all current neighbors to point a
        for neighbor in neighbors: #for all neighbors
            edge = (current, neighbor) #an edge will be (a,b)
            if edge not in circuit and (neighbor, current) not in circuit: #check if (a,b) or (b,a) is not in circuit
                self.graph[current].remove(neighbor) #remove neighbor from neighborhood
                self.graph[neighbor].remove(current) #vica versa 
                self.euler_circuit_util(neighbor, circuit) #recurse
                break  # Break to avoid further exploration if a neighbor is found
        circuit.append(current)


# Debug
# G1
print('1. Debug')
print('\ta. G1')
g = Graph()
g.add_edge('a', 'b')
g.add_edge('b', 'e')
g.add_edge('e', 'c')
g.add_edge('c', 'd')
g.add_edge('d', 'e')
g.add_edge('e', 'a')
g.euler_circuit()