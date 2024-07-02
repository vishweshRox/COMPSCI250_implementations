#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:05:46 2024

@author: vishweshpalani
"""

class Surd:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, o):
        return Surd(self.a + o.a, self.b + o.b)
    def __sub__(self, o):
        return Surd(self.a - o.a, self.b - o.b)
    def __mul__(self, o):
        return Surd(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)
    def __str__(self):
        return str(self.a) + " + " + str(self.b) + "*sqrt(2)"
        

w = {}
w[0] = Surd(400, 0)
w[1] = Surd(350, 0)

for i in range(2,85):
    w[i] = Surd(0, 1) * w[i - 1] - w[i - 2] + Surd(700, 0) - Surd(0, 350)
    
k=84
print(str(k) + " : " + str(w[k]))