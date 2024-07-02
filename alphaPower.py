#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:16:47 2024

@author: vishweshpalani
"""

a1 = ["a", "aa", "aaa"]
a2 = ["b", "ab", "aab"]

alphabet = a1

n = 200

for j in range(n + 1):
    
    temp = [""]
    
    for i in range(j):
        new_temp = []
        for s in temp:
            for letter in alphabet:
                new_str = s + letter
                if not new_str in new_temp: new_temp.append(new_str)
        temp = new_temp
        
    print("n = " + str(j))
    print("length: " + str(len(temp)))
    #print(temp)
    print("________")