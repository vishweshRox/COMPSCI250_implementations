#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:19:22 2024

@author: vishweshpalani

"""
def print_path(parent, start, goal):
    path = [goal]
    current = goal
    while current != start:
        if current in parent:
            current = parent[current]
            path.append(current)
        else:
            print("No path exists from", start, "to", goal)
            return
    path.reverse()
    print("Path from", start, "to", goal, ":", "->".join(path))
    
def next(frontier, priority):
    temp  = "dummy"
    m = 1000000
    for state in frontier:
        if priority[state] < m:
            m = priority[state]
            temp = state
    return temp
        

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes  # list of node strings
        self.edges = edges  # DICT key string - string tuple, value is the edge cost
        self.neighbors = {}
        for node in self.nodes:
            self.neighbors[node] = []
            for edge in self.edges:
                if edge[0] == node:
                    self.neighbors[node].append(edge[1])
    
    def search(self, start, goal):
        frontier = []
        priority = {}
        for node in self.nodes:
            priority[node] = 1000
        explored = set()
        parent = {} #constructs moving forward key string, value string, parent[s1] = s2, s2 is the parent of s1
                
        frontier.append(start)
        priority[start] = 0
        
        while(len(frontier) > 0):
            
            cur = next(frontier, priority)
            frontier.remove(cur)
            explored.add(cur)
            
            if cur == goal: break
            
            base_cost = priority[cur]
            
            for successor in self.neighbors[cur]: #successor is also a string
                step_cost = self.edges[(cur, successor)]
                
                if not successor in explored:
                    path_cost = base_cost + step_cost
                    
                    if not successor in frontier: frontier.append(successor)
                    
                    if path_cost < priority[successor]: 
                        priority[successor] = path_cost
                        parent[successor] = cur
                        
        print("PATH COST: " + str(priority[goal]))
        print_path(parent, start, goal)
        
cities = ["Montpelier", "Augusta", "Albany", "Concord", "Boston", "Amherst", "Hartford", "Providence"]
edges1 = {
    ("Montpelier", "Augusta"):180, 
    ("Montpelier", "Concord"):117, 
    ("Montpelier", "Amherst"):153, 
    ("Montpelier", "Albany"):158, 
    ("Augusta", "Concord"):163, 
    ("Augusta", "Boston"):166, 
    ("Concord", "Boston"):68, 
    ("Concord", "Amherst"):97, 
    ("Boston", "Providence"):51, 
    ("Boston", "Hartford"):102,
    ("Boston", "Amherst"):95, 
    ("Hartford", "Providence"):74, 
    ("Hartford", "Amherst"):53,  
    ("Hartford", "Albany"):113,
    ("Amherst", "Albany"):101,
         }

edges2 = {}
for edge in edges1:
    edges2[edge] = edges1[edge]
    edges2[(edge[1], edge[0])] = edges2[edge]
    
g1 =  Graph(cities, edges2)

for city in cities:
    if city != "Boston":
        g1.search(city, "Boston")
        
                        
                
                
            
            
            
            
        
        

                
                
    
    


    