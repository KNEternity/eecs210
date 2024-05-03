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
        About: add edges to graph
        Input: vertex(string)
        Output: none
        """
        self.graph[u].add(v)
        self.graph[v].add(u)
        
    def is_euler_circuit(self):
        """
        About: check if there is a euler circuit in the graph
        Input: none
        Output: boolean
        """
        for vertex in self.graph: 
            if len(self.graph[vertex]) % 2 != 0:
                return False
        return True 
    
    def euler_circuit(self): 
        """
        About: print if euler circuit is not possible and odd vertexes, else print the entire circuit
        Input: none
        Output: print statement / none
        """
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
        """
        About: helps to check euler circuit
        Input: vertex(str), circuit(set)
        Output: none
        """
        neighbors = list(self.graph[current]) #list out all current neighbors to point a
        for neighbor in neighbors: #for all neighbors
            edge = (current, neighbor) #an edge will be (a,b)
            if edge not in circuit and (neighbor, current) not in circuit: #check if (a,b) or (b,a) is not in circuit
                self.graph[current].remove(neighbor) #remove neighbor from neighborhood
                self.graph[neighbor].remove(current) #vica versa 
                self.euler_circuit_util(neighbor, circuit) #recurse
                break  # Break to avoid further exploration if a neighbor is found
        circuit.append(current)

    def has_hamiltonian_circuit(self):
        """
        About: Check's if graph might/has a hamilton circuit based on Dirac's Theorem
        Input: none
        Output: print statement
        """
        num_vertices = len(self.graph)
        for vertex in self.graph:
            if len(self.graph[vertex]) < num_vertices / 2:
                return "might have a Hamilton circuit based on Dirac's Theorem"
        return "has a Hamilton circuit based on Dirac's Theorem"

    def has_hamiltonian_circuit_ore(self):
        """
        About: Check's if graph might/has a hamilton circuit based on Ore's Theorem
        Input: none
        Output: print statement
        """
        num_vertices = len(self.graph)
        for u in self.graph:
            for v in self.graph:
                if u != v and v not in self.graph[u] and u not in self.graph[v]:
                    if len(self.graph[u]) + len(self.graph[v]) < num_vertices:
                        return "might have a Hamilton circuit based on Ore's Theorem"
        return "has a Hamilton circuit based on Ore's Theorem"



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
# G2
print('\tb. G2')
a = Graph()
a.add_edge('a', 'b')
a.add_edge('b', 'e')
a.add_edge('e', 'c')
a.add_edge('c', 'b')
a.add_edge('c', 'd')
a.add_edge('d', 'e')
a.add_edge('d', 'a')
a.add_edge('e', 'a')
a.euler_circuit()
# G3
print('\tc. G3')
c = Graph()
c.add_edge('a', 'b')
c.add_edge('a', 'd')
c.add_edge('a', 'c')
c.add_edge('b', 'd')
c.add_edge('b', 'e')
c.add_edge('c', 'd')
c.add_edge('d', 'e')
c.euler_circuit()
# Bridge
print('\td. Bridge')
d = Graph()
d.add_edge('a', 'b')
d.add_edge('b', 'a')
d.add_edge('a', 'c')
d.add_edge('c', 'a')
d.add_edge('a', 'd')
d.add_edge('c', 'd')
d.add_edge('b', 'd')
d.euler_circuit()
print()
# Test
print('1. Test')
t = Graph()
t.add_edge('a', 'b')
t.add_edge('a', 'd')
t.add_edge('b', 'd')
t.add_edge('b', 'e')
t.add_edge('b', 'c')
t.add_edge('c', 'f')
t.add_edge('d', 'e')
t.add_edge('d', 'g')
t.add_edge('e', 'f')
t.add_edge('e', 'h')
t.add_edge('f', 'h')
t.add_edge('f', 'i')
t.add_edge('g', 'h')
t.add_edge('h', 'i')
t.euler_circuit()
print()
# Debug
# G1
print('2. Debug')
print('\ta. G1')
print(f'\t\t{g.has_hamiltonian_circuit()}')
# G2
print('\tb. G2')
print(f'\t\t{a.has_hamiltonian_circuit()}')
# G3
print('\tc. G3')
print(f'\t\t{c.has_hamiltonian_circuit()}')
print()
# Test
print('2. Test')
t = Graph()
t.add_edge('a', 'b')
t.add_edge('a', 'c')
t.add_edge('b', 'c')
t.add_edge('c', 'f')
t.add_edge('d', 'f')
t.add_edge('d', 'e')
t.add_edge('e', 'f')
print(f'\t\t{t.has_hamiltonian_circuit()}')
print()
# Debug
# G1
print('3. Debug')
print('\ta. G1')
print(f'\t\t{g.has_hamiltonian_circuit_ore()}')
# G2
print('\tb. G2')
print(f'\t\t{a.has_hamiltonian_circuit_ore()}')
# G3
print('\tc. G3')
print(f'\t\t{c.has_hamiltonian_circuit_ore()}')
print()
# Test
print('3. Test')
print(f'\t\t{t.has_hamiltonian_circuit_ore()}')
print()