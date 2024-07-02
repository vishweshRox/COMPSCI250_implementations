#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:19:22 2024

@author: vishweshpalani

"""
def print_path(parent, start, goal):
    path = [str(goal)]
    current = goal
    while current != start:
        if current in parent:
            current = parent[current]
            path.append(str(current))
        else:
            print("No path exists from", start, "to", goal)
            return
    path.reverse()
    print("Path from", start, "to", goal, ":", "->".join(path))
    
def next(frontier, priority, heuristic):
    temp  = "dummy"
    m = 1000000
    for state in frontier:
        if priority[state] + heuristic[state] < m:
            m = priority[state] + heuristic[state]
            temp = state
    return temp
        

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes  # list of node strings
        self.edges = edges  # DICT key tuple - tuple tuple, value is the edge cost
        self.neighbors = {}
        for node in self.nodes:
            self.neighbors[node] = []
            for edge in self.edges:
                if edge[0] == node:
                    self.neighbors[node].append(edge[1])
    
    def search(self, start, goal, heuristic=lambda x : 0):
        frontier = []
        priority = {}
        hStore = {}
        for node in self.nodes:
            priority[node] = 1000
            hStore[node] = heuristic(node)
        explored = set()
        parent = {} #constructs moving forward key string, value string, parent[s1] = s2, s2 is the parent of s1
                
        frontier.append(start)
        priority[start] = 0
        
        step = 0
        
        while(len(frontier) > 0):
            
            print("___________________________________")    
            print("STEP: ", step)
            print("FRONTIER: ", frontier)
            print("EXPLORED: ", explored)
            print("___________________________________") 
            
            cur = next(frontier, priority, hStore)
            frontier.remove(cur)
            explored.add(cur)
            
            if cur == goal: break
            
            base_cost = priority[cur]
            
            
            for successor in self.neighbors[cur]: #successor is also a string
                step_cost = self.edges[(cur, successor)]
                
                if not successor in explored:
                    path_cost = base_cost + step_cost
                    
                    if not successor in frontier: frontier.append(successor)
                    
                    if path_cost < priority[successor]: #no need to adjust for heuristic here, heuristic of the same node will be the same
                        priority[successor] = path_cost
                        parent[successor] = cur
            
            step += 1
                        
        print("PATH COST: " + str(priority[goal]))
        print_path(parent, start, goal)
        
locs = []
edges = {}
n = 4
        
for i in range(n + 1):
    for j in range(n + 1):
        locs.append((i, j))

for loc in locs:
    i = loc[0]
    j = loc[1]
    if j % 2 == 0 and i < n:
        edges[(loc, (i+1, j))] = 3 #east
    if j % 2 != 0 and i > 0:
        edges[(loc, (i-1, j))] = 3 #west
    if i % 2 == 0 and j < n:
        edges[(loc, (i, j+1))] = 1 #north
    if i % 2 != 0 and j > 0:
        edges[(loc, (i, j-1))] = 1 #south
    
    
g1 =  Graph(locs, edges)


print("UCS")
g1.search((1,1), (3,3))

print()

print("A*")
g1.search((1,1), (3,3), lambda t : (3 - t[0]) * 3 + (3 - t[1]) * 1)
        
                        
                
                
            
            
            
            
        
        

                
                
    
    


    